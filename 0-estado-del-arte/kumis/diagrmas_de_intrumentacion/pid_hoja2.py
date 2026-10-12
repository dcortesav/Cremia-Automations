from pidlib import *
def hoja2(path_png,path_svg=None):
    fig,ax=new()
    frame(ax,"2 de 2","P&ID-L3-002 · LÍNEA 3: KUMIS","Fermentación, envasado, fin de línea y maduración fría")
    legend(ax)
    XS=[48,68,88,108,128]; Yt=104
    # entrada
    offpage(ax,2,100,"DE HOJA 1"); T(ax,7.5,95.5,"22 a 26 °C",fs=5)
    P(ax,[(13,100),(22,100),(22,125.5),(131,125.5)]); fa(ax,18,100,"r"); fa(ax,22,112,"u")
    # sala limpia
    ax.add_patch(Rectangle((36,82.5),102,44.3,fc="none",ec=GY,lw=1.0,ls=(0,(6,3)),zorder=1))
    T(ax,87,81.0,"SALA DE FERMENTACIÓN: presión positiva +20 a +30 Pa, filtros HEPA H14",fs=5.2,b=True,c=GY)
    bub(ax,143,112,"PDT","510",True); imp(ax,140.3,112,138,112); T(ax,143,106.6,"sala",fs=4.6)
    for i,x in enumerate(XS):
        P(ax,[(x+3,125.5),(x+3,120.4)]); valve(ax,x+3,122.9,"" if i else "XV-502","onoff","v",act=1,tagpos=(x-3,122.9)) if i==0 else valve(ax,x+3,122.9,"","onoff","v",act=1)
        tank(ax,x,Yt,12,28,f"FM-50{i+1}","2.000 L" ,agit=True,jacket=True,tf=5.8)
        P(ax,[(x,Yt-16.4),(x,84)]); valve(ax,x,87.2,"" if i else "XV-503","onoff","v",act=-1,tagpos=(x+5.5,87.2)) if i==0 else valve(ax,x,87.2,"","onoff","v",act=-1)
    T(ax,88,78.6,"FM-502 a FM-505: instrumentación y válvulas idénticas a FM-501",fs=5.0,it=True)
    P(ax,[(48,84),(150,84)])
    # instrumentos FM-501
    bub(ax,58,114,"LT","501"); imp(ax,55.3,114,54,114)
    bub(ax,58,105,"AT","501"); imp(ax,55.3,105,54,105); T(ax,58,101.2,"pH",fs=4.6)
    bub(ax,34,106,"TT","501"); imp(ax,36.7,106,42,106) if False else P(ax,[(36.7,106),(42,106)],"imp")
    bub(ax,28,98,"TIC","501",True); sig(ax,[(34,103.3),(34,102),(28,102),(28,100.7)])
    P(ax,[(40.7,90),(26,90)],"ah"); valve(ax,35,90,"TV-501","ctl","h",act=1,tagpos=(35,85.8)); T(ax,24.5,92.2,"AC/AH",fs=4.8,c=BL,ha="left")
    sig(ax,[(30.7,98),(35,98),(35,95.9)])
    # inoculo
    ax.add_patch(Rectangle((26,111),10,8,fc="white",ec=BK,lw=1.1,zorder=3)); T(ax,31,116,"CUL-501",fs=5.4,b=True); T(ax,31,113.3,"Cultivo DVS",fs=4.8)
    P(ax,[(36,115),(42,115)]); valve(ax,39,115,"VP-501","onoff","h",act=1,tagpos=(39,111.3),fs=5)
    T(ax,26,121,"Inoculación",fs=4.8,it=True,ha="left"); T(ax,26,119.4,"aséptica ciega",fs=4.8,it=True,ha="left")
    # envasado
    P(ax,[(150,84),(150,84)]); pump(ax,146,84,"P-601")
    ax.add_patch(Circle((158,84),3.2,fc="white",ec=BK,lw=1.1,zorder=4)); ax.plot([155.9,160.1],[81.7,86.3],color=BK,lw=0.8,zorder=5)
    T(ax,158,77.8,"FL-601",fs=5.6,b=True); T(ax,158,75.9,"Tamiz",fs=5)
    P(ax,[(161.2,84),(178,84)]); fa(ax,168,84,"r")
    bub(ax,140,92,"PT","601"); imp(ax,140,89.3,140,84)
    bub(ax,152,92,"TT","601"); imp(ax,152,89.3,152,84)
    tank(ax,172,108,8,12,"ES-601","Esencia",tf=5.2)
    P(ax,[(172,100.6),(172,97)]); pump(ax,172,94.6,"","d",r=2.2); P(ax,[(172,92.4),(172,84)]); T(ax,166.2,94.6,"P-603",fs=5.2,b=True)
    bub(ax,179,97,"FQ","601"); imp(ax,176.3,97,173.9,95.5)
    ax.add_patch(Rectangle((178,76),18,16,fc="white",ec=BK,lw=1.3,zorder=3)); T(ax,187,86,"EN-601",fs=6.4,b=True); T(ax,187,83,"Envasadora",fs=5.2); T(ax,187,80.8,"cabina ISO 5",fs=5.2); T(ax,187,78.4,"UV / H₂O₂",fs=4.8)
    bub(ax,185,69,"LT","601"); P(ax,[(185,71.7),(185,76)],"imp")
    # zona discreta
    ax.add_patch(Rectangle((36,43),160,26,fc="none",ec=GY,lw=0.9,ls=(0,(6,3)),zorder=1)); T(ax,39,45.2,"ZONA DISCRETA: sellado, codificado, inspección, encajonado, paletizado y maduración fría",fs=5.2,ha="left",b=True,c=GY)
    YD=56
    def blk(x,tag,name,w=14,h=10):
        ax.add_patch(Rectangle((x-w/2,YD-h/2),w,h,fc="white",ec=BK,lw=1.3,zorder=3)); T(ax,x,YD+1.3,tag,fs=6,b=True); T(ax,x,YD-1.7,name,fs=4.9)
    blks=[(184,"SL-601","Sellado induc."),(166,"CI-601","Codif. láser/CIJ"),(148,"TE-601","Termoencog."),(130,"INS-601","Visión + peso"),(112,"ENC-601","Encajonadora"),(94,"R-601","Robot paletiz."),(76,"TF-701","Túnel 0 a 2 °C"),(58,"CF-701","Cámara 2 a 4 °C")]
    for x,t,n in blks: blk(x,t,n)
    P(ax,[(187,76),(187,62),(184,62),(184,61)])
    for xa,xb in [(177,173),(159,155),(141,137),(123,119),(105,101),(87,83),(69,65)]:
        for dy in (-1.2,1.2): ax.plot([xa,xb],[YD+dy,YD+dy],color=BK,lw=0.9,zorder=2)
        fa(ax,(xa+xb)/2,YD,"l")
    bub(ax,126,66,"AT","601"); P(ax,[(126,63.3),(128,YD+5)],"imp"); bub(ax,134,66,"WT","601"); P(ax,[(134,63.3),(133,YD+5)],"imp")
    bub(ax,112,66,"ZS","601"); P(ax,[(112,63.3),(112,YD+5)],"imp")
    bub(ax,94,66,"XS","601"); P(ax,[(94,63.3),(94,YD+5)],"imp")
    bub(ax,76,66,"TT","701"); P(ax,[(76,63.3),(76,YD+5)],"imp")
    bub(ax,58,66,"TT","702"); P(ax,[(58,63.3),(58,YD+5)],"imp"); bub(ax,50,66,"AT","701"); P(ax,[(50,63.3),(52,YD+5)],"imp"); T(ax,50,62.2,"HR",fs=4.6)
    # CIP
    ax.add_patch(Rectangle((10,26),26,14,fc="white",ec=BK,lw=1.3,zorder=3)); T(ax,23,35.8,"CIP-901",fs=6.4,b=True); T(ax,23,32.4,"Skid CIP",fs=5.4); T(ax,23,29.6,"NaOH 2 %, HNO₃ 1 %",fs=4.8)
    P(ax,[(36,36),(190,36)],"cip"); P(ax,[(36,30),(190,30)],"cip"); fa(ax,110,36,"r",GN); fa(ax,110,30,"l",GN)
    T(ax,120,38.6,"Suministro CIP: fermentadores, tuberías, tamiz, envasadora y equipos de la hoja 1",fs=5.2,c=GN,b=True); T(ax,120,27.6,"Retorno CIP",fs=5.2,c=GN,b=True)
    for xx,l in ((68,"a FM-501 a FM-505"),(112,"a hoja 1 (TM-401, PA-401)"),(158,"a FL-601 y EN-601")):
        P(ax,[(xx,36),(xx,40.2)],"cip"); valve(ax,xx,40.2,"","onoff","v",act=1) if False else None
        T(ax,xx,41.7,l,fs=4.6,c=GN)
    for xx,f,n in ((44,"AT","901"),(52,"AT","902"),(60,"TT","901"),(68,"FT","901")):
        bub(ax,xx,23.6,f,n,True); P(ax,[(xx,26.3),(xx,30)],"imp")
    ax.text(4,127.7,"Parámetros: inoculación a 22 a 26 °C (cultivo mesófilo) · fermentación 14 a 18 h hasta pH 4,50 a 4,60 · rotura y enfriamiento a 10 a 12 °C · envasado a 8 a 12 °C · maduración a 2 a 4 °C.",fontsize=5.8,color=GY,zorder=6,va="center")
    fig.savefig(path_png,dpi=200,facecolor="white")
    if path_svg: fig.savefig(path_svg,facecolor="white")
    plt.close(fig)
if __name__=="__main__": hoja2("h2_test.png")
