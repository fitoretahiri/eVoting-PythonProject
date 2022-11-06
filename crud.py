class CRUD:
    def insertDataToUser(sqlConn):
        name = input("Shkruaj emrin qe deshironi te shtoni: ")
        role = input(f"Cfare roli do te kete {name}: ")
        cursor = sqlConn.cursor()
        cursor.execute(
            'Insert into useri (emri, roli) values(?,?)',
            (name,role))
        sqlConn.commit()
        sqlConn.close()

    def getUserData(sqlConn):
        cursor = sqlConn.cursor()
        cursor.execute("Select * from useri")
        for row in cursor:
            print(f'{row}')
        sqlConn.close()

    def updateUserData(sqlConn):
        id = int(input('Shkruani ID te userit qe deshironi te nderroni: '))
        name = input("Shkruani emrin e ri: ")
        cursor = sqlConn.cursor()
        cursor.execute(
            'update useri set emri = ? where id = ?',(name,id)
        )
        sqlConn.commit()
        sqlConn.close()

    def deleteUser(sqlConn):
        id = int(input("Cilin user deshironi te fshini: "))
        cursor = sqlConn.cursor()
        cursor.execute(
            'delete from useri where id=?',(id)
        )
        sqlConn.commit()
        sqlConn.close()

    def getUserRole(sqlConn, nrID):
        #id = int(input("Shkruani ID tuaj per tu verifikuar se jeni admin: "))
        cursor = sqlConn.cursor()
        cursor.execute(
            'select roli from useri where id=?',(nrID)
        )
        for row in cursor:
            return row.roli
    
    def getCandidates(sqlConn):
        cursor = sqlConn.cursor().execute(
            'select * from candidate'
        )
        for row in cursor:
            print(f'{row.emri} {row.mbiemri} {row.partiaPolitike}:  {row.id}')

    def insertCandidate(sqlConn):
        name = input("Shkruaj emrin e kandidatit: ")
        surname = input("Shkruaj mbiemrin e kandidatit: ")
        partia = input("Shkruaj partine politike te kandidatit: ")
        
        cursor = sqlConn.cursor();
        cursor.execute(
            'Insert into candidate (emri, mbiemri, partiaPolitike) values(?,?,?)',
            (name,surname,partia))
        sqlConn.commit()

    def updateCandidate(sqlConn):
        id = int(input('Shkruani ID te kandidatit qe deshironi te beni update: '))
        name = input("Shkruani emrin e ri: ")
        surname = input("Shkruani mbiemrin e ri: ")

        cursor = sqlConn.cursor()
        cursor.execute(
            'update candidate set emri = ?, mbiemri=? where id = ?',(name,surname,id)
        )
        sqlConn.commit()

    def deleteCan(sqlConn):
        id = int(input("Cilin kandidat deshironi te fshini: "))
        cursor = sqlConn.cursor()
        cursor.execute(
            'delete from candidate where id=?',(id)
        )
        sqlConn.commit()

    def vote(conn):
        id = int(input('Zgjedhni numrin e kandidatit qe deshironi ta votoni: '))
        conn.cursor().execute(
            'update candidate set votat=votat+1 where id=?',(id)
        )
        conn.commit()
    
    def shfaqRezultatin(sqlConn):
        cursor = sqlConn.cursor().execute(
            'select * from candidate'
        )
        for row in cursor:
            print(f'{row.emri} {row.mbiemri} {row.partiaPolitike} {row.votat}')
    
    def getFituesi(conn):
        cursor=conn.cursor().execute(
            'select emri,mbiemri from candidate where votat=(Select max(votat) from candidate)'
        )
        for row in cursor:
            return f'{row.emri} {row.mbiemri}'