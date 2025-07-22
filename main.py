import argparse
import commands

def add_subcommand(sub_commands):
    parser_add = sub_commands.add_parser("add", help='''
                                         Digite o nome do tópico/matéria entre aspas "Matemática Aplicada" caso a matéria seja composta
                                         de 2 ou mais palavras, caso contrário, será utilizado apenas a primeira palavra.
                                         Digite -r caso queira relacionar essa matéria com uma outra (exemplo: "Matemática Aplicada" -r Matemática)
                                         '''
                                         , description='Esse comando permite você adicionar uma nova matéria para sua sessão de estudos.')
    parser_add.add_argument('-r', nargs='*')
    parser_add.add_argument('subject', type=str)
    return parser_add

def list_subcommand(sub_commands):
    return sub_commands.add_parser("list", description='Lista todas as matérias cadastradas no sistema.')

def focus_subcommand(sub_commands):
    parser_focus = sub_commands.add_parser("focus", description='Começa uma nova sessão de foco')
    parser_focus.add_argument('-s', type=str)
    parser_focus.add_argument('-e', action="store_true")
    return parser_focus

def log_subcommand(sub_commands):
     pass

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
    parser_add = add_subcommand(sub_commands)

    #subcommand list
    parser_list = list_subcommand(sub_commands)

    #subcommand focus
    parser_focus = focus_subcommand(sub_commands)

    args = parser.parse_args()
    if args.command == "add":
        commands.add_study_session(args.subject, args.r)
    elif args.command == "focus":
         if getattr(args, "s"):
            commands.start_focus_session(args.s)
         if getattr(args, "e"):
              commands.end_focus_sessions()
    elif args.command == "list":
         parser_list.set_defaults(function=commands.list_studys_session(True))
    

if __name__ == '__main__':
        main()