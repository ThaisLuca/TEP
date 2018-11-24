import java.util.*;
import org.junit.*;


public class BloomFilterTest {

	private BloomFilter filtro;
	private static int NUMERO_TERMOS = 2000;
	private static int TAMANHO_MAX = 1000;

	@BeforeClass
	public void setUpClass(){
		Random random = new Random(100);
		Set<Long> termos = new HashSet<Long>();
		for(int i = 0; i < NUMERO_TERMOS; i++){
			termos.add((long) random.nextInt(TAMANHO_MAX));
		}
	}

	@Before
	public void setUp(){
		filtro = new BloomFilter(4 * NUMERO_TERMOS, 4);
	}

	@Test 
	public void testarAdicionarNovosTermos(){
		for(long t: termos){
			filtro.adicionarTermo(t);
		}
		assertFalse(filtro.filtroVazio());
	}
}