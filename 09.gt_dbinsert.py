import pymysql
import os
import gt_place

def MakeDB(place_kp):
    db_result=[]

    conn=pymysql.connect(
        user='root',
        passwd='210714',
        host='127.0.0.1',
        db='final_gt_table',
        charset='utf8'        
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)


    if place_kp!=';':
        insert_class_sql = "REPLACE INTO gt_table (`filename`,`O01001`,`O01002`,`O01003`,`O01004`,`O01005`,`O01006`,`O01007`,`O01008`,`O01009`,`O02010`,`O02011`,`O02012`,`O02013`,`O03014`, `O03015`,`O03016`,`O03017`,`O04018`,`O04019`,`O04020`,`O04021`,`O05022`,`O05023`,`O05024`,`O05025`,`O05026`,`O06027`,`O06028`,`O06029`,`O06030`,`O07031`,`O07032`,`O07033`,`O07034`,`O07035`,`O08036`,`O08037`,`O08038`,`O09039`,`O09040`,`O09041`,`O09042`,`O10043`,`O10044`,`O10045`,`O11046`,`O11047`,`O11048`,`O12049`,`O12050`,`O12051`,`O12052`,`O12053`,`O12054`,`O12055`,`I01001`,`I01002`,`I01003`,`I01004`,`I01005`,`I01006`,`I01007`,`I02008`,`I02009`,`I02010`,`I03011`,`I03012`,`I03013`,`I04014`,`I04015`,`I05016`,`I05017`,`I05018`,`I06019`,`I06020`,`I07021`,`I08022`,`I08023`,`I08024`,`I09025`,`I09026`,`I09027`,`I09028`,`I09029`,`I09030`,`I09031`,`I09032`) VALUES"+ place_kp
        db_result.append(insert_class_sql)
        cursor.execute(insert_class_sql)

    result = cursor.fetchall()

    conn.commit()
    conn.close()


    return db_result



if __name__ == '__main__':
    MakeDB(gt_place.count_place(gt_place.main_path))
