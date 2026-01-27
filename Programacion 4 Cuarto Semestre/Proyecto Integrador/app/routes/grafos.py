from flask import Blueprint, render_template, request, session, redirect, url_for, flash, abort
from ..models import db, Usuario, RutaFavorita
import networkx as nx
from app.models import db, Usuario, RutaFavorita, EstadoMapa

grafos_bp = Blueprint('grafos', __name__)

def obtener_grafo():
    G = nx.Graph()
    
    # Lista Maestra
    # Nombres de interés y añade del "1" al "320"
    nodos_totales = [
        "Esq_Sup_Izq", "Esq_Sup_Der", "Esq_Inf_Izq", "Esq_Inf_Der", 
        "Nucleo_Laberinto"] + [str(i) for i in range(1, 321)]
    
    # Registramos todos los nodos en el grafo
    G.add_nodes_from(nodos_totales)

    # Lista de conexiones o aristas
    conexiones = [
    ("Esq_Sup_Izq", "1"), ("1", "2"), ("2", "3"), ("2", "6"), ("3", "4"),
    ("4", "5"), ("5", "11"), ("6", "10"), ("6", "7"), ("10", "11"),
    ("7", "8"), ("8", "9"), ("8", "15"), ("9", "157"), ("157", "154"),
    ("154", "155"), ("154", "153"), ("155", "156"), ("153", "152"), ("152", "156"),
    ("152", "151"), ("156", "158"), ("158", "159"), ("159", "160"), ("159", "170"),
    ("170", "169"), ("170", "171"), ("169", "174"), ("171", "172"), ("174", "175"),
    ("172", "173"), ("173", "175"), ("175", "176"), ("176", "177"), ("177", "178"),
    ("178", "179"), ("177", "181"), ("181", "182"), ("181", "180"), ("182", "183"),
    ("183", "184"), ("184", "185"), ("183", "186"), ("186", "187"), ("187", "188"),
    ("188", "189"), ("189", "190"), ("189", "195"), ("190", "191"), ("191", "192"),
    ("192", "194"), ("Esq_Inf_Izq", "194"), ("192", "193"), ("193", "196"), ("195", "196"),
    ("180", "200"), ("200", "199"), ("199", "197"), ("196", "197"), ("197", "198"),
    ("194", "198"), ("198", "205"), ("205", "206"), ("206", "207"), ("207", "208"),
    ("208", "212"), ("212", "216"), ("216", "217"), ("217", "218"), ("218", "219"),
    ("218", "220"), ("220", "221"), ("221", "222"), ("222", "223"), ("223", "224"),
    ("224", "220"), ("224", "225"), ("225", "226"), ("226", "227"), ("227", "228"),
    ("228", "229"), ("229", "230"), ("230", "231"), ("231", "232"), ("232", "227"),
    ("232", "233"), ("233", "234"), ("234", "235"), ("235", "239"), ("239", "Esq_Inf_Der"),
    ("Esq_Inf_Der", "238"), ("238", "237"), ("237", "236"), ("235", "236"), ("236", "291"),
    ("291", "289"), ("289", "290"), ("289", "288"), ("288", "287"), ("290", "287"),
    ("287", "286"), ("286", "292"), ("286", "298"), ("292", "293"), ("293", "294"),
    ("294", "308"), ("294", "295"), ("295", "296"), ("296", "297"), ("297", "124"),
    ("124", "123"), ("124", "125"), ("123", "122"), ("122", "121"), ("122", "101"),
    ("101", "102"), ("101", "86"), ("86", "85"), ("85", "84"), ("84", "87"),
    ("84", "83"), ("83", "82"), ("82", "81"), ("81", "Esq_Sup_Der"), ("81", "79"),
    ("79", "80"), ("79", "78"), ("78", "77"), ("77", "76"), ("77", "89"),
    ("89", "88"), ("88", "87"), ("76", "75"), ("75", "74"), ("74", "71"),
    ("71", "70"), ("71", "72"), ("70", "69"), ("69", "68"), ("68", "65"),
    ("68", "72"), ("72", "73"), ("73", "92"), ("92", "91"), ("91", "93"),
    ("91", "90"), ("93", "94"), ("90", "95"), ("95", "96"), ("96", "97"),
    ("97", "98"), ("97", "109"), ("109", "110"), ("109", "108"), ("108", "107"),
    ("108", "119"), ("119", "120"), ("120", "121"), ("107", "106"), ("106", "87"),
    ("106", "105"), ("105", "104"), ("104", "103"), ("103", "102"), ("110", "129"),
    ("110", "111"), ("129", "128"), ("128", "127"), ("127", "126"), ("126", "125"),
    ("125", "319"), ("319", "318"), ("318", "317"), ("317", "315"), ("315", "314"),
    ("314", "316"), ("314", "313"), ("313", "312"), ("312", "311"), ("311", "310"),
    ("310", "309"), ("310", "300"), ("309", "308"), ("300", "299"), ("300", "301"),
    ("299", "298"), ("301", "302"), ("302", "303"), ("303", "305"), ("303", "304"),
    ("304", "275"), ("275", "270"), ("275", "276"), ("276", "285"), ("276", "277"),
    ("285", "298"), ("285", "284"), ("277", "278"), ("278", "279"), ("279", "282"),
    ("279", "280"), ("282", "283"), ("283", "284"), ("280", "281"), ("281", "233"),
    ("270", "269"), ("269", "271"), ("269", "268"), ("271", "272"), ("272", "273"),
    ("273", "274"), ("268", "267"), ("268", "247"), ("247", "248"), ("247", "246"),
    ("246", "225"), ("246", "245"), ("245", "244"), ("244", "243"), ("243", "242"),
    ("245", "242"), ("242", "241"), ("242", "249"), ("249", "248"), ("249", "261"),
    ("241", "240"), ("240", "215"), ("215", "214"), ("215", "209"), ("214", "213"),
    ("213", "212"), ("209", "210"), ("209", "207"), ("210", "211"), ("210", "250"),
    ("211", "253"), ("211", "201"), ("201", "204"), ("201", "202"), ("204", "200"),
    ("204", "167"), ("202", "199"), ("202", "203"), ("167", "168"), ("167", "166"),
    ("166", "165"), ("166", "257"), ("257", "256"), ("257", "258"), ("256", "255"),
    ("255", "254"), ("253", "252"), ("252", "254"), ("252", "251"), ("251", "250"),
    ("251", "258"), ("248", "264"), ("264", "263"), ("263", "262"), ("262", "265"),
    ("262", "260"), ("260", "258"), ("265", "267"), ("305", "306"), ("306", "307"),
    ("111", "112"), ("112", "113"), ("113", "98"), ("113", "114"), ("98", "99"),
    ("99", "100"), ("100", "67"), ("67", "66"), ("66", "64"), ("64", "65"),
    ("64", "62"), ("62", "61"), ("61", "63"), ("61", "50"), ("63", "118"),
    ("118", "117"), ("117", "116"), ("117", "55"), ("55", "56"), ("55", "54"),
    ("54", "53"), ("53", "52"), ("52", "58"), ("52", "51"), ("51", "57"),
    ("57", "56"), ("51", "49"), ("49", "50"), ("49", "48"), ("48", "45"),
    ("48", "38"), ("45", "46"), ("45", "33"), ("46", "47"), ("33", "34"),
    ("33", "32"), ("32", "31"), ("31", "27"), ("27", "13"), ("27", "26"),
    ("26", "28"), ("28", "29"), ("28", "34"), ("29", "30"), ("38", "35"),
    ("35", "34"), ("35", "36"), ("36", "37"), ("37", "25"), ("25", "26"),
    ("25", "24"), ("24", "14"), ("24", "23"), ("14", "15"), ("14", "12"),
    ("12", "13"), ("12", "11"), ("15", "16"), ("16", "18"), ("16", "19"),
    ("19", "17"), ("19", "20"), ("18", "21"), ("21", "22"), ("22", "23"),
    ("22", "148"), ("23", "43"), ("43", "42"), ("43", "44"), ("42", "41"),
    ("41", "40"), ("40", "39"), ("39", "38"), ("114", "115"), ("115", "116"),
    ("44", "60"), ("60", "59"), ("60", "141"), ("59", "58"), ("141", "140"),
    ("141", "142"), ("148", "149"), ("148", "147"), ("149", "150"), ("150", "151"),
    ("150", "162"), ("160", "161"), ("161", "162"), ("162", "163"), ("163", "168"),
    ("163", "164"), ("164", "144"), ("144", "143"), ("143", "142"), ("144", "145"),
    ("145", "147"), ("145", "146"), ("59", "132"), ("132", "131"), ("132", "139"),
    ("139", "138"), ("138", "137"), ("138", "140"), ("137", "259"), ("259", "260"),
    ("259", "136"), ("136", "266"), ("266", "265"), ("266", "135"), ("135", "134"),
    ("134", "307"), ("134", "133"), ("133", "130"), ("130", "115"), ("130", "131"),
    ("7", "320"), ("320", "8"), ("Nucleo_Laberinto", "131"), ("Nucleo_Laberinto", "139"), ("Nucleo_Laberinto", "133"),
    ("Nucleo_Laberinto", "136")
]
    
    for nodo_a, nodo_b in conexiones:
        if nodo_a and nodo_b:  # Evita errores con strings vacíos
            G.add_edge(nodo_a, nodo_b, weight=1)
        
    return G

def verificar_grafo(G):
    print("\n=== REVISIÓN DE CONEXIONES === ")
    aislados = list(nx.isolates(G))
    if aislados:
        print(f"NODOS OLVIDADOS: {aislados}")
    else:
        print("No hay nodos aislados.")
    
    componentes = list(nx.connected_components(G))
    if len(componentes) > 1:
        print(f"GRAFO ROTO: Hay {len(componentes)} grupos aislados.")
    else:
        print("Grafo totalmente conectado.")

@grafos_bp.route('/limpiar_bloqueos', methods=['POST'])
def limpiar_bloqueos():
    # Esta función ahora solo redirige, ya que eliminamos la persistencia automática de SESION_ACTUAL
    return redirect(url_for('grafos.index'))

@grafos_bp.route('/guardar_favorita', methods=['POST'])
def guardar_favorita():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main.home'))

    nombre = request.form.get('nombre_ruta_personalizado')
    origen = request.form.get('origen_fav')
    destino = request.form.get('destino_fav')
    bloqueos = request.form.get('bloqueos_fav')

    if not nombre or not origen or not destino:
        flash("ERROR: DATOS DE RUTA INCOMPLETOS")
        return redirect(url_for('grafos.index'))

    try:
        nueva_ruta = RutaFavorita(
            user_id=user_id,
            nombre_ruta=nombre,
            origen=origen,
            destino=destino,
            bloqueos=bloqueos
        )
        db.session.add(nueva_ruta)
        db.session.commit()
        flash(f"MEMORIA ACTUALIZADA: RUTA '{nombre.upper()}' REGISTRADA")
    except Exception as e:
        db.session.rollback()
        flash("ERROR CRÍTICO: NO SE PUDO GUARDAR")
            
    return redirect(url_for('grafos.index'))

# --- SECCIÓN ADMINISTRATIVA ACTUALIZADA ---

@grafos_bp.route('/admin/usuarios')
def panel_admin():
    if session.get('rol') != 'admin':
        abort(403) 
    usuarios = Usuario.query.all()
    return render_template('admin_panel.html', usuarios=usuarios)

@grafos_bp.route('/admin/cambiar_rango/<int:id>/<nuevo_rol>')
def cambiar_rango(id, nuevo_rol):
    # Solo el usuario ID 1 puede acceder a esta función
    if session.get('user_id') != 1:
        abort(403)
    
    usuario = Usuario.query.get(id)
    if usuario:
        if usuario.id == 1:
            flash("OPERACIÓN DENEGADA: El rango del administrador central no puede ser alterado")
        elif nuevo_rol == 'admin':
            flash("OPERACIÓN DENEGADA: No se pueden designar nuevos administradores")
        else:
            usuario.rol = nuevo_rol
            db.session.commit()
            flash(f"NIVEL DE ACCESO ACTUALIZADO: {usuario.username.upper()} -> {nuevo_rol.upper()}")
    
    return redirect(url_for('grafos.panel_admin'))

@grafos_bp.route('/admin/eliminar_usuario/<int:id>')
def eliminar_usuario(id):
    # Solo el usuario ID 1 puede eliminar
    if session.get('user_id') != 1:
        abort(403)
        
    user = Usuario.query.get(id)
    if user:
        if user.id == 1:
            flash("ERROR CRÍTICO: No se puede eliminar la unidad central")
        else:
            db.session.delete(user)
            db.session.commit()
            flash(f"UNIDAD {user.username.upper()} DESCONECTADA")
    
    return redirect(url_for('grafos.panel_admin'))

@grafos_bp.route('/admin/actualizar_bloqueos_globales', methods=['POST'])
def actualizar_bloqueos_globales():
    # Solo el ID 1 (Admin Central) tiene permiso
    if session.get('user_id') != 1:
        abort(403)
    
    # IMPORTANTE: El nombre debe coincidir con el 'name' del input en el HTML
    bloqueos = request.form.get('nodos_bloqueados_lista', '') 
    
    estado = EstadoMapa.query.get(1)
    if estado:
        estado.nodos_restringidos = bloqueos
        db.session.commit()
        flash("SISTEMA ACTUALIZADO: RESTRICCIONES GLOBALES PUBLICADAS")
    else:
        # Si por alguna razón no existe el ID 1, lo crea
        nuevo_estado = EstadoMapa(id=1, nodos_restringidos=bloqueos)
        db.session.add(nuevo_estado)
        db.session.commit()
        
    return redirect(url_for('grafos.index'))

# --- VISTA PRINCIPAL DEL MAPA ---

@grafos_bp.route('/', methods=['GET', 'POST'])
def index():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main.home'))

    G = obtener_grafo()
    
    # --- BLOQUEOS GLOBALES DEL ADMINISTRADOR ---
    estado = EstadoMapa.query.get(1)
    bloqueos_admin = estado.nodos_restringidos.split(',') if estado and estado.nodos_restringidos else []
    
    for nodo in bloqueos_admin:
        if nodo in G:
            for vecino in list(G.neighbors(nodo)):
                G[nodo][vecino]['weight'] = 9999 # Bloqueo global
    # --------------------------------------------

    resultado = None
    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        bloqueados_raw = request.form.get('nodos_bloqueados_lista', '')

        # Bloqueos temporales del usuario actual
        nodos_usuario = bloqueados_raw.split(',') if bloqueados_raw else []
        for nodo in nodos_usuario:
            if nodo in G:
                for vecino in list(G.neighbors(nodo)):
                    G[nodo][vecino]['weight'] = 9999

        # Cálculo de ruta
        if origen in G and destino in G:
            try:
                camino = nx.dijkstra_path(G, origen, destino, weight="weight")
                costo = nx.dijkstra_path_length(G, origen, destino, weight="weight")
                resultado = {
                    "origen": origen, "destino": destino,
                    "bloqueados_str": bloqueados_raw,
                    "camino_nodos": camino, "costo": costo
                }
            except nx.NetworkXNoPath:
                resultado = {"error": "Sin ruta"}

    return render_template('grafos.html', res=resultado, bloqueos_globales=bloqueos_admin)