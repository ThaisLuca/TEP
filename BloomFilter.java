import java.util.*;
import java.lang.Long;
import sun.nio.*;

class BloomFilter {
	private boolean[] espacos;
	private int tamanho;
	private int hash;


	//Construtor
	public BloomFilter(int tamanho, int hash) {
		this.tamanho = tamanho;
		this.hash = hash;
		this.espacos = new boolean[tamanho];
	}

 
	public boolean filtroVazio() {
		return tamanho == 0;
	}

	public int getTamanho() {
		return tamanho;
	}

	public void adicionarTermo(long termo){
		int[] res = calcularEspacos(termo);
		for(int e : res){
			this.espacos[e] = true;
		}
	}

	public boolean buscarTermo(Long termo){
		int[] res = calcularEspacos(termo);
		for(int esp : res){
			if(!this.espacos[esp]){
				return false;
			}
		}
		return true;
	}

	private int[] calcularEspacos(long termo){
		int[] esp = new int[hash];
		for(int i = 0; i < hash; i++){
			esp[i] = calcularHash(termo, i);
		}
		return esp;
	}

	private int calcularHash(long termo, int i){
		return Math.abs(Long.valueOf(termo*i).hashCode()) % this.tamanho;
	}

	public static void main(String[] args){
		BloomFilter f = new BloomFilter(4, 2);
		f.adicionarTermo(2);
		if(!f.filtroVazio()){
			System.out.println("Vazio");
		}
		System.out.println(f.buscarTermo((long) 2));
	}
}