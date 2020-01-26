package br.ce.tce.hackathon.dao;

import java.io.BufferedReader;
import java.io.FileReader;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.PostConstruct;

//import javax.ejb.Stateless;

//import javax.ejb.Stateless;

import br.ce.tce.hackathon.modelo.Gasto;

/**
 * Classe para carregamento dos dados
 * Obs1: atualmente carrega de arquivo 
 * Obs2: Pode ser configurada para consumir um repositório (tipo firebase) ou banco de dados (relacional ou NoSql)
 * @author charles.marques
 *
 */
//@Stateless
public class DAO {
	
//	@PersistenceContext
//	private EntityManager entityManager;
	
	private static List<Gasto> gastos = new ArrayList<Gasto>();
	
	private static Map<Long, Gasto> banco = new HashMap<Long, Gasto>();
	
//	@PostConstruct
	protected void loadData() {
		SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
		gastos = new ArrayList<>();
		Gasto gasto;
		System.out.println("GastoDao foi criado");
		Boolean primeiro = Boolean.TRUE;
		String[] data;
		Date dia;
		try {
			BufferedReader csvReader = new BufferedReader(new FileReader("/home/suporte/Workspace/meudeputado/src/resources/gastos_candidatos.csv"));
			String row;
			while ((row = csvReader.readLine()) != null) {
			    data = row.split(";");
			    
			    if (primeiro) {
			    	primeiro = false;
			    	continue;
			    }
				// deputado descricao data valor
			    dia = sdf.parse(data[2]);
				gasto = new Gasto(data[0], data[1], new Double(data[3].replace(',', '.')), dia);
				gastos.add(gasto);
			}
			csvReader.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		gastos.forEach(f -> adiciona(f));
	}
	
	public DAO() {
		loadData();
	}
	
	public void adiciona(Gasto gasto) {
		Long id = (new Integer(banco.size()).longValue());
		banco.put(id, gasto);
	}
	
	public Gasto busca(Long id) {
		return banco.get(id);
	}
	
	public Gasto remove(Long id) {
		return banco.remove(id);
	}

//	public Gasto atualiza(Gasto gasto) {
//		return banco.put(gasto.getId(), gasto);
//	}

	public List<Gasto> getGastos() {
		return gastos;
	}

	public void setGastos(List<Gasto> gastos) {
		DAO.gastos = gastos;
	}
}