### Progetto Bioinformatica

E' stata implementata una funzione che ha come argomento un vertice v e restituisce tutti i vertici raggiungibili da v.

La funzione in questione è get_reachable_vertices_from(vertex) all'interno della classe GFA in ./pygfa/gfa.py. La funzione utilizza una struttura dati per insiemi disgiunti manipolabile grazie al nuovo codice aggiunto in ./pygfa/algorithms/disjoint_sets.py

per testare la funzione è stato creato inoltre il file
./get_reachable_vertices.py
    utilizzo:
        python3 get_reachable_vertices.py [-h] -f gfa_file -v vertex

Marco Caspani (829546)
