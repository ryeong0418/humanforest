import pymysql
import os
import maskjsonsize

def MakeDB(result_kp):
    db_result = []
    
    conn = pymysql.connect(
        user='root',
        passwd='210714',
        host='127.0.0.1',
        db='finalmasksize',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

 
    # createTable_bb_sql = ''
    # cursor.execute(createTable_bb_sql)

    if result_kp!= ';':
        insert_class_sql = "replace INTO  mask_objectsize (`filename`,`M42`) VALUES"+ result_kp
        db_result.append(insert_class_sql)
        cursor.execute(insert_class_sql)

    result = cursor.fetchall()

    conn.commit()
    conn.close()


    return db_result



if __name__ == '__main__':
    MakeDB(maskjsonsize.count_annot(maskjsonsize.main_path))