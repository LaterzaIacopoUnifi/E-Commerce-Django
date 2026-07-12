# Laterza E-Commerce --- **Studente:** Iacopo Laterza (Matricola: 7136664)  
**Tipologia di Progetto:** Full-Stack Web Application  
**Framework:** Django (Python)  

---

## Descrizione
Questa applicazione simula il comportamento di un vero e proprio E-Commerce, un sito di compravendita per qualsiasi tipo di oggetto, interamente sviluppato in Django. 

Il sistema implementa una gestione dinamica dei ruoli che permette agli utenti di interagire con la piattaforma in base ai propri permessi: gli utenti standard possono acquistare prodotti, i lavoratori possono gestire il catalogo e i manager possono fondare e amministrare intere attività commerciali.

---

## Features Implementate per Ruolo

L'applicazione gestisce una gerarchia di permessi a 4 livelli:

### 1. Utente Standard (`NormalUser`)
*   Registrazione, Login e Logout.
*   Navigazione del catalogo prodotti.
*   Inserimento dei prodotti nel carrello.
*   Gestione e pagamento del carrello finale.
*   Visualizzazione e cancellazione della cronologia degli ordini.

### 2. Lavoratore (`Worker`)
*   Include tutte le funzionalità dell'utente standard.
*   Permesso speciale per creare ed eliminare gli oggetti associati al Business in cui lavora.

### 3. Capo Azienda (`Manager`)
*   Include tutte le funzionalità del lavoratore.
*   Permesso speciale per creare e dare vita a nuovi Business, collegando ad essi i prodotti messi in vendita.

### 4. Amministratore (`Admin`)
*   Include tutte le funzionalità del manager.
*   Accesso completo al pannello di amministrazione di Django per la gestione totale del database (creazione e modifica di utenti di qualsiasi tipo, prodotti e attività).

---

## Scenario di Test 
Per verificare il corretto funzionamento del sito , consiglio di:
1. **Test Registarzione/Login** : Appena cliccate il link, il sito vi porta alla pagina principale. In alto a destra troverete i bottoni "Registrati" e "Accedi": se volete creare un nuovo profilo allora cliccate su "Registrati" ; altrimenti nel caso volete accedere ad un profilo esistente cliccate su "Accedi"
2. **Test Inserimento Oggetti nel carrello** : Dopo aver effettuato il login/ la registrazione di un qualsiasi tipo di untente , nella pagina principale provate a cliccare sul tasto "Aggiungi al Carrello" e vedere apparire un numero in alto a destra dove si trova il blocco Carrello.
3. **Test Effettuare Pagamento** : Dopo aver effettuato il login/ la registrazione di un qualsiasi tipo di untente e dopo aver aggiunto dei prodotti al carrello, nella pagina principale cliccate sul blocco Carrello e visionate gli oggetti aggiunti al carrello e poi provate a cliccare su "Vai al Pagamento". Subito dopo vi porterà ad una pagina che , dopo aver inserito l'indirizzo di spedizione e dopo aver scelto il metodo di pagamento, cliccate su "Vai al pagamento" per effettuare l'acquisto dei prodotti del carrello
4. **Test Creazione Prodotto** : Dopo essersi collegati come Worker/Manager , nella pagina principale cliccate sul bottone Business e il sito vi porterà in una nuova pagina dove potete aggiungere un prodotto a seconda dell'azienda di cui fate parte. Capiterà che, nel caso di un nuovo Worker/Manager il sito chieda a quale azienda volete lavorare. Dopo Aver scelto potete tranquillamente aggiungere tutti i prodotti che volete
5. **Test Eliminazione Prodotto**: Dopo essersi collegati come Worker/Manager , nella pagina principale cliccate sul bottone "Elimina Prodotto" di un prodotto che volete eliminare e noterete che il prodotto verrà eliminato dal sito e dalla lista dei prodotti totali che Laterza E-Commerce vuole vendervi
6. **Test Creazione Business**: Dopo essersi collegati come Manager , nella pagina principale cliccate sul bottone "Business" , dove vi porterà alla gestione del vostro Business. Da qui potrete creare un nuovo Business e nel caso decidere di dovrà diventare il proprietario dell'attività.
7. **Test Ricerca Prodotti**: In qualsiasi momento la barra della ricera sia disponibile , è possibile cercare i prodotti attraverso la barra di ricerca. Molto comodo soprattutto se non ci si ricordasse del nome del prodotto che vogliamo comprare
8. **Test Informazioni Prodotti**: Per ogni prodotto è possibile controllare maggiori informazioni semplicemente cliccando sul blocco che identifica l'oggetto. 
9. **Test Informazioni Prodotti di un Business**: Nel caso volessimo sapere tutti gli oggetti venduti da una sola attività , basterà toccare il nome dell'attività nel blocco che identifica il prodotto in vendita

---
## Istruzioni per l'Installazione Locale

Segui questi passaggi per clonare ed avviare il progetto sul tuo computer:

1. **Clona il repository:**
   ```bash
   git clone [https://github.com/LaterzaIacopoUnifi/E-Commerce-Django.git](https://github.com/LaterzaIacopoUnifi/E-Commerce-Django.git)
   
2. **Entra nella cartella del progetto:**
   ```bash
   cd E-Commerce-Django
3. **Crea e attiva un ambiente virtuale:**
   * Windows:
      ```bash
      python -m venv .venv 
      .venv\Scripts\activate
   * Mac/Linux:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
  
1. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt

1. **Applica le migrazioni:**
   ```bash
   python manage.py migrate
  
1. **Avvia il server::**
   ```bash
    python manage.py runserver

L'applicazione sarà disponibile all'indirizzo locale: http://127.0.0.1:8000/

   

###  Database e Account Demo
Il repository include il file `db.sqlite3`, pre-popolato con dati demo realistici (utenti, profili, attività e prodotti) per permettere l'esplorazione immediata di tutte le funzionalità del sito.

**Account Demo Disponibili:**

| Ruolo | Username | Password |
| :--- | :--- | :--- |
| **Normal User** | `user_normaluser` | `demoDemoUs3r` |
| **Worker** | `user_worker` | `demoDemoWork3r` |
| **Manager** | `user_manager` | `demoDemoManag3r` |
| **Admin** | `admin1234` | `1234` |

---

###  Link al Deployment
Il progetto è online e raggiungibile al seguente indirizzo:  
🔗 [https://iaclat.pythonanywhere.com/](https://iaclat.pythonanywhere.com/)

---
*Progetto sviluppato per il corso PROGETTAZIONE E PRODUZIONE MULTIMEDIALE  2025-2026 .*
  