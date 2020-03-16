class SqlService():
    @staticmethod
    def create_update(table, cols, valuses, updatecols):
        colname = '(`' + '`,`'.join(cols) + '`)'
        updatecolname = [i + '=values(' + i + ')'  for i in updatecols]
        updatecolname = ','.join(updatecolname)
        valls = []
        for value in valuses:
            value = [str(i) for i in value]
            value = "('" + "','".join(value) + "')"
            valls.append(value)

        values = ','.join(valls)
        sqlstr = 'insert into ' + '`' + table + '` ' + colname + ' values ' + values + ' on duplicate key update '+ updatecolname
        return sqlstr

    @staticmethod
    def create_insert(table, cols, valuses):
        colname = '(`' + '`,`'.join(cols) + '`)'
        valls = []
        for value in valuses:
            value = [str(i) for i in value]
            value = "('" + "','".join(value) + "')"
            valls.append(value)

        values = ','.join(valls)
        sqlstr = 'insert into ' + '`' + table + '` ' + colname + ' values ' + values
        return sqlstr


