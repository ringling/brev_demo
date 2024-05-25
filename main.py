from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/prisvarsling/health-check", methods=['GET'])
def health_check():
    return {"Datakilder": {
        'Status': 'Ok',
        'Ksd':{'ExtTS': "yyyymmdd", "VersionTime": "yyyymmdd"},
        'Aftaler':{'ExtTS': "yyyymmdd", "VersionTime": "yyyymmdd"},
        'AftaleDaekninger':{'ExtTS': "yyyymmdd", "VersionTime": "yyyymmdd"},
        'Prisbilag':{"Caching": False},
        'SplitterIndbetalere':{'ExtTS': "yyyymmdd", "VersionTime": "yyyymmdd"}
        }
      }

# prisvarsling/0000000001/brev?fra_valoer=yyyymmdd&til_valoer=yyyymmdd
@app.route("/prisvarsling/<aftale_part>/brev")
def brev_build(aftale_part, methods=['GET']):
    fra_valoer = request.args.get('fra_valoer')
    til_valoer = request.args.get('til_valoer')
    print(fra_valoer, til_valoer)
    d = {"Aftalepart": aftale_part, "Modtager": "Test firma2",
         "DaekningGruppe": ["Dækning 1", "Dækning 2", "Dækning 3a"]}
    return d