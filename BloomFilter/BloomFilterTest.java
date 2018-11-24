import java.util.*;
import org.junit.*;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * Autor: Thais Luca
 * Tópicos Especiais em Programação - Departamento de Ciência da Computação, UFRJ
 * 23/11/18
 */

/**
 * Classe para testar o Bloom Filter
 */
@RunWith(JUnit4.class)
public class BloomFilterTest {

    private static ArrayList<Long> termos;
    private BloomFilter filtro;
    private static int NUMERO_TERMOS = 2000;
    private static int TAMANHO_MAX = 10000;

    @BeforeClass
    public static void setUpClass(){
        termos =  new ArrayList<Long>();
        Random random = new Random(100);
        for(int i = 0; i < NUMERO_TERMOS; i++){
            termos.add((long) random.nextInt(TAMANHO_MAX));
        }
    }

    @Before
    public void setUp(){
        filtro = new BloomFilter(4 * NUMERO_TERMOS, 2);
    }

    @Test
    public void testarAdicionarNovosTermos(){
        for(long t: termos){
            filtro.adicionarTermo(t);
        }
        assertFalse(filtro.filtroVazio());
    }

    @Test
    public void testarVerdadeiroPositivo(){
        filtro.adicionarTermo((long) 324);
        assertTrue(filtro.buscarTermo((long) 324));
    }

    @Test
    public void testarVerdadeiroNegativo(){
        assertFalse(filtro.buscarTermo(TAMANHO_MAX + 1));
    }

    @Test
    public void testarLista(){
        int termosEncontrados = 0;
        int falsosPositivos = 0;
        int falsosNegativos = 0;
        int verdadeirosPositivos = 0;
        int verdadeirosNegativos = 0;

        adicionarTermos();

        for(long i = 0; i < TAMANHO_MAX; i++){
            boolean termoEncontrado = filtro.buscarTermo(i);
            if(termoEncontrado){
                termosEncontrados++;
            }
            if(termos.contains(i)){
                if(!termoEncontrado) {
                    falsosNegativos++;
                } else {
                    verdadeirosPositivos++;
                }
            } else {
                if(termoEncontrado) {
                    falsosPositivos++;
                }
                else {
                    verdadeirosNegativos++;
                }
            }
        }

        System.out.println("Número de termos encontrados: " + termosEncontrados);
        System.out.println("Número de verdadeiros positivos: " + verdadeirosPositivos);
        System.out.println("Número de verdadeiros negativos: " + verdadeirosNegativos);
        System.out.println("Número de falsos positivos: " + falsosPositivos);
        System.out.println("Número de falsos negativos: " + falsosNegativos);
    }

    private void adicionarTermos(){
        for(long t: termos){
            filtro.adicionarTermo(t);
        }
    }
}