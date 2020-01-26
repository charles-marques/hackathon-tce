import 'package:flutter/material.dart';

void main() => runApp(Meudeputadoapp());

class Meudeputadoapp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
            body: ListaDeputados(),
            appBar: AppBar(
              title: Text('Deputados'),
            ),
        )
    );
  }
}

class ListaDeputados extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        ItemDeputado(Deputado('FERNANDO HUGO', 48900.00)),
        ItemDeputado(Deputado('DELEGADO CAVALCANTE', 27000.00)),
        ItemDeputado(Deputado('MIRIAN SOBREIRA', 30000.00)),
        ItemDeputado(Deputado('OSMAR BAQUIT', 33788.00)),
        ItemDeputado(Deputado('ACRÍSIO SENA', 47600.00)),
        ItemDeputado(Deputado('TIN GOMES', 32700.00)),
        ItemDeputado(Deputado('VITOR VALIM', 30500.00)),
        ItemDeputado(Deputado('RENATO ROSENO', 32778.00)),
      ],
    );
  }
}

class ItemDeputado extends StatelessWidget{

  final Deputado _deputado;

  ItemDeputado(this._deputado);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        leading: Icon(Icons.people),
        title: Text(_deputado.nome.toString()),
        subtitle: Text(_deputado.valor.toString()),


      ),
    );
  }
}

class Deputado {
  final String nome;
  final double valor;
  //final int numeroConta;

  Deputado(this.nome, this.valor);
}