import json
import plotly
from flask import Flask, request, render_template
import warnings
from company_name import company
from stock_analysis import stock_analysis

warnings.filterwarnings("ignore")

app = Flask(__name__, template_folder="template")


@app.route('/', methods=["GET", "POST"])
def analyse():
    if request.method == "POST":
        user_input = request.form.get("companyTickerCode")
        company_code = str(user_input)
        company_name = company.getCompanyName(company_code)
        figure = stock_analysis.analyseStockForCompanyTickerCode(ticker=company_code, name=company_name)
        graphJSON = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("index.html", graphJSON=graphJSON)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port="7077")
