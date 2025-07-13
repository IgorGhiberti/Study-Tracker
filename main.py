import argparse
import commands

def main():
    parser = argparse.ArgumentParser(prog="Study Tracker", description="Ajuda os estudantes a controlarem sua rotina/produtividade nos estudos!")
    sub_commands = parser.add_subparsers(title='Subcommands',
                                       description='''
                                        add: Adiciona uma nova seção de estudos
                                        focus: Inicia uma seção de foco do tópico/matéria escolhido
                                        log: Exibe logs, por padrão diários, dos dias estudados e a quantidade de horas
                                        cal: Permite a criação de um calendário de estudos, definindo a matéria, dia e objetivos
                                        ach: Exibe as conquistas adquiridas pelo estudante
                                        ''', dest="command", required=True)

    #subcommand add    
    parser_add = sub_commands.add_parser("add", help='''
                                         Digite o nome do tópico/matéria entre aspas "Matemática Aplicada" caso a matéria seja composta
                                         de 2 ou mais palavras, caso contrário, será utilizado apenas a primeira palavra.
                                         Digite -r caso queira relacionar essa matéria com uma outra (exemplo: "Matemática Aplicada" -r Matemática)
                                         '''
                                         , description='Esse comando permite você adicionar uma nova matéria para sua sessão de estudos.')
    
    #Argumentos através de flags tem que ser usados no terminal, por ex:
    #python3 main.py add (command) -s (argumento via flag) "Nome do subject"
    parser_add.add_argument('-r', nargs='*')

    #Ou, através de argumentos posicionais, nesse caso, o subject seria o primeiro argumento, então seria:
    #python3 main.py add "Nome do subject"
    parser_add.add_argument('subject', type=str)

    #subcommand list
    parser_list = sub_commands.add_parser("list")

    parser_list.set_defaults(function=commands.list_studys_session())

    args = parser.parse_args()
    if args.command == "add":
        commands.add_study_session(args.subject, args.r)
    #elif args.command == "list":
     #    commands.list_studys_session()
    

if __name__ == '__main__':
        main()