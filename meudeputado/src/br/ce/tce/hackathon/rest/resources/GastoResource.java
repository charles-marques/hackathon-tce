package br.ce.tce.hackathon.rest.resources;

import java.net.URI;
import java.util.stream.Collectors;

import javax.inject.Inject;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import com.google.gson.Gson;
import com.thoughtworks.xstream.XStream;

import br.ce.tce.hackathon.dao.DAO;
import br.ce.tce.hackathon.modelo.Gasto;

@Path("gastos")
public class GastoResource {

//	@Inject
	DAO dao = new DAO();
	
	@Path("{id}")
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public String busca(@PathParam("id") long id) {
		try {
			Gasto gasto = dao.busca(id);
			return gasto.toJSON();
		} catch (NullPointerException e) {
			Exception excecao = new Exception("NÃO ENCONTRADO!");
			return new Gson().toJson(excecao);
		}
	}
	
	@Path("/")
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public String busca(@PathParam("ano") Integer ano) {
		try {
//			Gasto gasto = dao.busca(ano);
//			resultado = dao.getGastos().stream().filter(f -> ano.equals(f.getData().getYear())).collect(Collectors.toList());
			return new Gson().toJson(dao.getGastos());
		} catch (NullPointerException e) {
			Exception excecao = new Exception("NÃO ENCONTRADO!");
			return new Gson().toJson(excecao);
		}
	}
	
//	@Path("/")
//	@POST
//	@Consumes(MediaType.APPLICATION_JSON)
//	public Response adicionarXML(String conteudo) {
//		Gasto gasto = (Gasto) new XStream().fromXML(conteudo);
//		
//		dao.adiciona(gasto);
//		
//		URI uri = URI.create("/gastos/" + gasto.getId());
//		return Response.created(uri).build();
//	}
//	
//	@Path("{id}/topicos/{topicoId}")
//	@DELETE
//	public Response removerProduto(@PathParam("id") long id, @PathParam("topicoId") long topicoId) {
//		Gasto gasto = dao.busca(id);
//		gasto.removeTopico(topicoId);
//		return Response.ok().build();
//	}
//	
//	@Path("{id}/topicos/{topicoId}")
//	@PUT
//	@Consumes(MediaType.APPLICATION_XML)
//	public Response atualizarProduto(@PathParam("id") long id, @PathParam("topicoId") long topicoId, String conteudo) {
//		Gasto gasto = dao.busca(id);
//		Topico topico = (Topico) new XStream().fromXML(conteudo);
//		gasto.troca(topico);
//		return Response.ok().build();
//	}
	
//	@Path("{id}/topicos/{topicoId}/titulo")
//	@PUT
//	@Consumes(MediaType.APPLICATION_XML)
//	public Response atualizarProdutoQuantidade(@PathParam("id") long id, @PathParam("topicoId") long topicoId, String conteudo) {
//		Gasto gasto = dao.busca(id);
//		Topico topico = (Topico) new XStream().fromXML(conteudo);
//		gasto.trocaTitulo(topico);
//		return Response.ok().build();
//	}
	
}