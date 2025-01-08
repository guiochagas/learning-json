import click

# Lista global para armazenar os itens
lista = []

@click.group()
def cli():
    """Um gerenciador simples de lista de tarefas."""
    pass

@click.command()
@click.argument('item')
def adicionar(item):
    """Adiciona um ITEM à lista."""
    lista.append(item)
    click.echo(f'Item "{item}" foi adicionado à lista.')

@click.command()
def mostrar():
    """Mostra os itens na lista."""
    if not lista:
        click.echo("A lista está vazia.")
    else:
        click.echo("Itens na lista:")
        for i, item in enumerate(lista, start=1):
            click.echo(f"{i}. {item}")

# Adiciona os comandos ao CLI principal
cli.add_command(adicionar)
cli.add_command(mostrar)

if __name__ == "__main__":
    cli()
