/**
 * Autor: Thais Luca
 * Tópicos Especiais em Programação - Departamento de Ciência da Computação, UFRJ
 * 23/11/18
 */

/**
 * Classe que representa um Bloom Filter
 */
public class BloomFilter {
    private boolean[] espacos;
    private int tamanho;
    private int hash;

    //Construtor
    public BloomFilter(int tamanho, int hash) {
        this.tamanho = tamanho;
        this.hash = hash;
        this.espacos = new boolean[tamanho];
    }

    /**
     * Verifica se o filtro está vazio
     * @return True se o filtro está vazio, False caso contrário
     */
    public boolean filtroVazio() {
        return tamanho == 0;
    }

    /**
     * Retorna o tamanho do filtro
     * @return tamanho do filtro em bytes
     */
    public int getTamanho() {
        return tamanho;
    }

    /**
     * Adiciona um termo ao filtro
     * @param termo o termo a ser adicionado
     */
    public void adicionarTermo(Long termo){
        int[] res = calcularEspacos(termo);
        for(int e : res){
            this.espacos[e] = true;
        }
    }

    /**
     * Verifica se um termo está no filtro
     * @param termo o termo a ser pesquisado
     * @return True se o termo está no filtro, False caso contrário
     */
    public boolean buscarTermo(long termo){
        int[] res = calcularEspacos(termo);
        for(int esp : res){
            if(!this.espacos[esp]){
                return false;
            }
        }
        return true;
    }

    /**
     * Calcula as posições para inserir o termo
     * @param termo o termo a ser inserido
     * @return o vetor contendo os endereços
     */
    private int[] calcularEspacos(long termo){
        int[] esp = new int[hash];
        for(int i = 0; i < hash; i++){
            esp[i] = calcularHash(termo, i);
        }
        return esp;
    }

    /**
     * Função hash para cálculo das posições de inserção
     * @param termo o termo a ser inserido
     * @param i o índice do termo na lista
     * @return o espaço para adicionar uma parte do termo
     */
    private int calcularHash(long termo, int i){
        return Math.abs(Long.valueOf(termo*i).hashCode()) % this.tamanho;
    }
}