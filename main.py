import argparse
import commands

def add_subcommand(sub_commands):
    parser_add = sub_commands.add_parser("add", help='''
                                         Adiciona uma nova matéria ao sistema de estudos.
                                         '''
                                         , description='''
                                        Use este comando para cadastrar uma nova matéria/tópico de estudo.
                                        
                                        Exemplo de uso:
                                        add "Matemática Aplicada"
                                        
                                        🔸 Dica: Use aspas se a matéria tiver mais de uma palavra.
                                        🔸 Relação entre matérias: use a flag -r para indicar que a nova matéria está relacionada com outra já existente.
                                        
                                        Exemplo:
                                        add "Cálculo 2" -r "Cálculo 1"
                                        ''')
    parser_add.add_argument('-r', nargs='*', help="(Opcional) Matérias relacionadas à matéria principal.")
    parser_add.add_argument('subject', type=str, help="Nome da matéria a ser adicionada.")
    return parser_add

def list_subcommand(sub_commands):
    return sub_commands.add_parser("list", help='Lista todas as matérias cadastradas no sistema.')

def focus_subcommand(sub_commands):
    parser_focus = sub_commands.add_parser("focus", help='Inicia ou finaliza uma sessão de foco.')
    parser_focus.add_argument('-s', type=str, help="Inicia uma nova sessão de foco para a matéria especificada.")
    parser_focus.add_argument('-e', action="store_true", help="Finaliza a sessão de foco atual.")
    return parser_focus

def log_subcommand(sub_commands):
    parser_log = sub_commands.add_parser("log", help='Exibe o histórico de estudos por dia.')
    parser_log.add_argument('-f', type=str, nargs='*', help="Filtra logs entre duas datas (formato: YYYY-MM-DD).")
    parser_log.add_argument('--full', action="store_true", help="Mostra o log completo de todos os dias estudados.")
    return parser_log

def main():
    parser = argparse.ArgumentParser(prog="Study Tracker", description="Ajuda os estudantes a controlarem sua rotina/produtividade nos estudos!")
    sub_commands = parser.add_subparsers(title='Subcommands',
                                       description='''
                                        add: Adiciona uma nova seção de estudos
                                        list: Lista todas as matérias cadastradas.
                                        focus: Inicia uma seção de foco do tópico/matéria escolhido
                                        log: Exibe logs, por padrão diários, dos dias estudados e a quantidade de horas
                                        ''', dest="command", required=True)

    #subcommand add
    parser_add = add_subcommand(sub_commands)

    #subcommand list
    parser_list = list_subcommand(sub_commands)

    #subcommand focus
    parser_focus = focus_subcommand(sub_commands)

    #subcommand log
    parser_log = log_subcommand(sub_commands)

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
    elif args.command == "log":
        if getattr(args, "f"): 
              commands.show_logs(args.f[0], args.f[1])
        elif getattr(args, "full"):
             commands.show_logs(full_time=True)
        else:
             commands.show_logs()
    

if __name__ == '__main__':
        main()