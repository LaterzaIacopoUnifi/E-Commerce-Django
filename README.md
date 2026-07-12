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
  