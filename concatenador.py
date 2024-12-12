import os

def check(file_name):
    if os.path.exists(file_name):
        answer = input(f"Arquivo de saída '{file_name}' já existe.\nDeseja sobrescrever? (y/n): ")
        if answer.lower() != 'y':
            print("Operação cancelada.")
            exit(-1)

def concat_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        # Escreve o cabeçalho apenas uma vez
        outfile.write("age,sex,chestPain,restingBloodPressure,serumCholestoral,fastingBloodSugar>120,restingEletroc,maximumHeartRate,exerciseInducedAngina,oldpeak,op_slope,numberMajorVessels,bloodFlow_thal,diagnosis\n")
        
        for file_name in file_list:
            if not os.path.exists(file_name):
                print(f"Arquivo não encontrado: {file_name}")
                continue

            try:
                with open(file_name, 'r') as f:
                    for line in f:
                        outfile.write(line)
                print(f"Arquivo '{file_name}' transcrito com sucesso.")
                        
            except Exception as e:
                print(f"Erro {file_name}: {e}")

if __name__ == '__main__':
    file_list = ['processed.cleveland.csv', 'processed.hungarian.csv', 'processed.switzerland.csv', 'processed.va.csv']
    output_file = 'data.csv'
    check(output_file)
    concat_files(file_list, output_file)