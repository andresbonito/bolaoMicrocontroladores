from flask import Flask, request, render_template, jsonify
from time import time

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web')

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form 
        data = data.to_dict(flat=False)
        print(data)

        with open(f'palpites/p_{str(int(time()))}.txt', 'w') as f:
            f.write('email;selecao_a;placa_a;selecao_b;placar_b;\n')
            f.write(f'{data["email"][0]};{data["selecao-a"][0]};{data["placar-a"][0]};{data["selecao-b"][0]};{data["placar-b"][0]};')

    return render_template('websocks.htm')

  
if __name__ == "__main__":
 app.run()