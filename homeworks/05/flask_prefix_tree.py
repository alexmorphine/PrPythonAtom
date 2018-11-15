from flask import Flask, request, jsonify

app = Flask(__name__)

class PrefixTree:
    #TODO реализация класса prefix tree, методы как на лекции + метод дать топ 10 продолжений. Скажем на строку кросс выдаем кроссовки, кроссовочки итп. Как хранить топ? 
    #Решать вам. Можно, конечно, обходить все ноды, но это долго. Дешевле чуток проиграть по памяти, зато отдавать быстро (скажем можно взять кучу)
    #В терминальных (конечных) нодах может лежать json с топ актерами.
    def __init__(self):
        self.root = [{}, {}]
        
    def add(self, string, freq):
        wrk_dict = self.root
        freq = int(freq)
        for n, i in enumerate(string):
            if i in wrk_dict[0]:
                if string[n:] not in wrk_dict[1]:
                    wrk_dict[1][string[n:]] = 0
                wrk_dict[1][string[n:]] += freq
                    
                wrk_dict[2] += freq
                wrk_dict = wrk_dict[0][i]
                
            else:
                
                wrk_dict[0][i] = [{}, {}]
                wrk_dict[1][string[n:]] = freq
                wrk_dict.append(freq)
                wrk_dict = wrk_dict[0][i]
        if self.check(string):
            return
        wrk_dict.append(True)
        #TODO добавить строку
        
    def check(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        if len(wrk_dict) != 2:
            return True
        return False
        #TODO проверить наличие строки
    
    def _check_part(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        return wrk_dict[1]
        #TODO проверить наличие строки как префикса
        
    def check_part(self, string):
        value = self._check_part(string)
        if value:
            return True
        return False
        
    def get_suggest(self, string):
        value = self._check_part(string)
        if value:
            print(value)
            suggests = [string + end for end in sorted(value, key=value.get, reverse=True)[:10]]
            return suggests
        return False
    
def init_prefix_tree(filename):
    pr_tree = PrefixTree()
    with open(filename, encoding='utf8') as f:
        for line in f:
            pr_tree.add(*line.strip().split('\t'))
    #TODO в данном методе загружаем данные из файла. Предположим вормат файла "Строка, чтобы положить в дерево" \t "json значение для ноды" \t частота встречаемости


@app.route("/get_sudgest/<string>", methods=['GET', 'POST'])
def return_sudgest(string):
    #TODO по запросу string вернуть json, c топ-10 саджестами, и значениями из нод
    return jsonify(top=pr_tree.get_suggest(string))

@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    return

if __name__ == "__main__":
    app.run()
