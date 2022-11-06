import crud as db
import pyodbc

sqlConn = pyodbc.connect(
        DRIVER='{SQL Server}',
        host = 'LAPTOP-0SN8DCT8',
        Database = 'eVoting',
        Trusted_Connection='yes',
        user = 'emri',
        password = '123'
    )

x = db.CRUD
id = int(input("Shkruani id per tu kyqur ne sistem: "))
role = x.getUserRole(sqlConn,id)
if role != 'admin' and role.lower() =='votues':
    print("Keta jane kandidatet ne dispozicion per tu votuar:\n")
    x.getCandidates(sqlConn)
    x.vote(sqlConn)
    print('Faleminderit per votim.')
else:
    print("Mire se vini ne platformen per votim!")

    while True:
        c = int(input("Keto jane komandat:\n1. Voto \n2. Shto Kandidate\n3. Shto user (votues)\n4. Perditso user (votues) \n5. Perditso kandidatin\n6. Fshij perdoruesin "+
        "\n7. Fshij kandidatin \n8. Shfaq rezultatin\n9. Shpall fituesin \nZgjedh:  "))
        if c == 1:
            x.vote(sqlConn)
        elif c==2:
            x.insertCandidate(sqlConn)
        elif c==3:
            x.insertDataToUser(sqlConn)
        elif c==4:
            x.updateUserData(sqlConn)
        elif c==5:
            x.updateCandidate(sqlConn)
        elif c==6:
            x.deleteUser(sqlConn)
        elif c==7:
            x.deleteCan(sqlConn)
        elif c==8:
            x.shfaqRezultatin(sqlConn)
        elif c==9:
            print(f'Fitues eshte: {x.getFituesi(sqlConn)}')
        choice=input('Vazhdo? Po\jo:  ').lower()
        if choice=='jo':
            break
            