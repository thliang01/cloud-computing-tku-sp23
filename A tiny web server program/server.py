

from flask import Flask, render_template_string

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return render_template_string('''
<form action="/" method="post">
      <p>Input 1: <input type="number" name="daily_calories" value="" id="val1"></p>
      <p>Input 2: <input type="number" name="daily_calories" value="" id="val2"></p>
      <input type="submit" value="Calculate" id="button_calculate">
      <p>Result: <input type="number" name="result_dc" value="" id="result"></p>
</form>
<script>
var val1_input = document.getElementById("val1");
var val2_input = document.getElementById("val2");
var result_input = document.getElementById("result");
var button_input = document.getElementById("button_calculate");
button_input.onclick = function(event) {
    result_input.value = parseFloat(val1_input.value) + parseFloat(val2_input.value);
    //event.preventDefault(); // don't send to server
    return false; // don't send to server
}
</script>
''')

if __name__ == '__main__':
    app.run(host="0.0.0.0")