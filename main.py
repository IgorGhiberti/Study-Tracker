import argparse

def main():
    parser = argparse.ArgumentParser(prog="Study Tracker", description="Ajuda os estudantes a controlarem sua rotina/produtividade nos estudos!")
    sub_commands = parser.add_subparsers(title='Subcommands',
                                       description='''
                                        add: Adiciona uma nova seção de estudos
                                        focus: Inicia uma seção de foco do tópico/matéria escolhido
                                        log: Exibe logs, por padrão diários, dos dias estudados e a quantidade de horas
                                        cal: Permite a criação de um calendário de estudos, definindo a matéria, dia e objetivos
                                        ach: Exibe as conquistas adquiridas pelo estudante
                                        ''')
                                       
    

    if __name__ == '__main__':
            main()