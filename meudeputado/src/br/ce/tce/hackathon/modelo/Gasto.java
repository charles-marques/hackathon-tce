package br.ce.tce.hackathon.modelo;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import com.google.gson.Gson;
import com.thoughtworks.xstream.XStream;

/**
 * 
 * @author charles.marques
 *
 */
@Entity
@Table(name = "gasto", schema = "deputado")
public class Gasto {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private String deputado;
	private String descricao;
	private Double valor;
	private Date data;

	public Gasto() {
	}

	public Gasto(String deputado, String descricao, Double valor, Date data) {
		super();
		this.deputado = deputado;
		this.descricao = descricao;
		this.valor = valor;
		this.data = data;
	}
	
	public Gasto(Long id, String descricao, String deputado, Double valor, Date data) {
		this(descricao, deputado, valor, data);
		this.id = id;
	}

	protected Long getId() {
		return id;
	}

	protected void setId(Long id) {
		this.id = id;
	}

	public String getDeputado() {
		return deputado;
	}

	public void setDeputado(String deputado) {
		this.deputado = deputado;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public Double getValor() {
		return valor;
	}

	public void setValor(Double valor) {
		this.valor = valor;
	}

	public Date getData() {
		return data;
	}

	public void setData(Date data) {
		this.data = data;
	}

	/* Others Methods */
	public String toXML() {
		return new XStream().toXML(this);
	}

	public String toJSON() {
		return new Gson().toJson(this);
//		return this.toString();
	}
}