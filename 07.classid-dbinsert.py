import pymysql
import os
import classid2

def MakeDB(result_kp):
    db_result = []
    
    conn = pymysql.connect(
        user='root',
        passwd='210714',
        host='127.0.0.1',
        db='inpainting_class_id',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

 
    # createTable_bb_sql = ''
    # cursor.execute(createTable_bb_sql)

    if result_kp!= ';':
        insert_class_sql = "REPLACE INTO inpainting (`filename`,`B000`,`BO01`,`BO02`,`BO03`,`BO04`,`BO05` ,`BO06`,`BO07`,`BO08`,`BO09`,`BO10`,`BO11`,`BO12`,`BO13`, `BO14`,`BO15`,`BI16`,`BI17`,`BI18`,`BI19`,`BI20`,`BI21`,`BI22`,`BI23`,`BI24`,`BI25`,`BI26`,`BI27`,`BI28`,`BI29`,`BI30`,`BI31`,`BI32`,`BI33`,`BI34`,`BI35`,`BI36`,`BI37`,`F38`,`F39`,`F40`,`F41`) VALUES"+ result_kp
        db_result.append(insert_class_sql)
        cursor.execute(insert_class_sql)

    result = cursor.fetchall()

    conn.commit()
    conn.close()


    return db_result



if __name__ == '__main__':
    MakeDB(classid2.count_annot(classid2.main_path))