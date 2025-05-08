from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <span style="text-align: center;"><h1 style="font-family: 'Arial', sans-serif;">F E R M I O N S</h1></span>
    <p style="font-family: 'Arial', sans-serif;">Fermions are the particles that make up matter — including atoms, stars, and everything we see in the universe. They are divided into two main categories: <a href="#leptons">leptons</a> and <a href="#quarks">quarks</a>. Leptons, such as electrons, are fundamental particles, while hadrons are composite particles made of quarks. Hadrons are further classified into mesons (quark–antiquark pairs) and baryons (such as protons and neutrons, made of three quarks).</p>
<p style="padding-bottom: 20px;"><img src="/static/Fermions.jpg" alt="Fermions" width="600"></p>
   

<h2 id="quarks" style="font-family: 'Arial', sans-serif;"><u>QUARKS</h2></u>
    <p style="font-family: 'Arial', sans-serif;">Quarks are elementary subatomic particles that form the building blocks of matter. There are six types, or 'flavors,' of quarks. Protons and neutrons are made of three quarks each: protons consist of two up quarks and one down quark (uud), while neutrons consist of one up quark and two down quarks (ddu).</p>
    <p style="font-family: 'Arial', sans-serif;">Each flavour of quark has a charge of either <b>+⅔e</b> (up, charm & top) or <b>-⅓e</b> (down, strange & bottom).</p>
    <p style="font-family: 'Arial', sans-serif;">The six flavours are;</p>
<ul style="font-family: 'Arial', sans-serif;">
    <li>Up</li>
    <li>Down</li>
    <li>Charm</li>
    <li>Strange</li>
    <li>Top</li>
    <li>Bottom</li>
</ul>
<img src="/static/Quarks.jpg" alt="Quarks" width="600"> <img src="/static/ProtonNeutronQuarks.jpg" alt="ProtonNeutronQuarks" width="600">

    <p style="font-family: 'Arial', sans-serif;">There are also six anti-quarks. Each anti-quark is identical to its counter-part, except it feature the opposite charge:</p>
    <p style="font-family: 'Arial', sans-serif;"><b>-⅔e</b> (anti-up, anti-charm & anti-top) and <b>+⅓e</b> (anti-down, anti-strange & anti-bottom).</p>
<img src="/static/AntiQuarks.jpg" alt="AntiQuarks" width="600">
    <p style="font-family: 'Arial', sans-serif;">Quarks also have a colour charge - <b style="color: red;">red</b>, <b style="color: green;">green</b> and <b style="color: blue;">blue</b> - which collectively make white.</p>
    <p style="font-family: 'Arial', sans-serif;" style="padding-bottom: 20px";><b>Note:</b> up and down quarks are the most common, as they form the protons and neutrons that make up all ordinary matter. The other quarks — charm, strange, top, and bottom — are less common and are typically found in high-energy processes like particle collisions, as well as in certain types of decay, such as alpha and beta decays.</p>
    


<h2 id="leptons" style="font-family: 'Arial', sans-serif;"><u>LEPTONS</h2></u>
    <p style="font-family: 'Arial', sans-serif;">There are also six flavours of Leptons;</p>
<ul style="font-family: 'Arial', sans-serif;">
    <li>Electron</li>
    <li>Muon</li>
    <li>Tau</li>
    <li>Electron Neutrino</li>
    <li>Muon Neutrino</li>
    <li>Tau Neutrino</li>
</ul>
   <p style="font-family: 'Arial', sans-serif;">Leptons are  elementary particles.</p>

"""

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

 
