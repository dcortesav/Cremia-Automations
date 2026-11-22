import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Ellipse, Wedge, FancyBboxPatch
BK="#111111"; BL="#1F6FB5"; RD="#C0392B"; GN="#2E8B57"; GY="#555555"
KIND={"p":(BK,2.0,"-"),"ah":(BL,1.5,"-"),"v":(RD,1.5,"-"),"sig":(GY,0.8,(0,(4,2))),"imp":(BK,0.7,"-"),"cip":(GN,1.4,(0,(6,2,1.5,2))),"air":(BL,1.1,(0,(3,2))),"cv":(BK,1.2,"-")}
def new(figsize=(17,11)):
    fig=plt.figure(figsize=figsize,facecolor="white"); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,200); ax.set_ylim(0,130); ax.axis("off"); ax.set_facecolor("white")
    return fig,ax
def P(ax,pts,kind="p",z=1):
    c,lw,ls=KIND[kind]; xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    ax.plot(xs,ys,color=c,lw=lw,ls=ls,zorder=z,solid_capstyle="butt",solid_joinstyle="miter")
def fa(ax,x,y,d,c=BK,s=1.2):
    t={"r":[(x-s,y+s*.7),(x-s,y-s*.7),(x+s,y)],"l":[(x+s,y+s*.7),(x+s,y-s*.7),(x-s,y)],"u":[(x-s*.7,y-s),(x+s*.7,y-s),(x,y+s)],"d":[(x-s*.7,y+s),(x+s*.7,y+s),(x,y-s)]}[d]
    ax.add_patch(Polygon(t,fc=c,ec=c,lw=0.3,zorder=4))
def T(ax,x,y,s,fs=6,ha="center",va="center",b=False,c=BK,rot=0,it=False):
    ax.text(x,y,s,fontsize=fs,ha=ha,va=va,fontweight="bold" if b else "normal",color=c,zorder=6,rotation=rot,style="italic" if it else "normal")
def bub(ax,x,y,f,n,dcs=False,r=2.7):
    ax.add_patch(Circle((x,y),r,fc="white",ec=BK,lw=0.9,zorder=5))
    if dcs: ax.plot([x-r,x+r],[y,y],color=BK,lw=0.7,zorder=6)
    ax.text(x,y+(0.95 if dcs else 0.0)+(0 if dcs else 0.95),f,ha="center",va="center",fontsize=5.6,zorder=7,color=BK)
    ax.text(x,y-1.25,n,ha="center",va="center",fontsize=5.4,zorder=7,color=BK)
def imp(ax,x1,y1,x2,y2): P(ax,[(x1,y1),(x2,y2)],"imp",2)
def sig(ax,pts): P(ax,pts,"sig",2)
def valve(ax,x,y,tag=None,kind="man",o="h",act=1,tagpos=None,fs=5.6):
    s=1.9;h=1.2
    if o=="h": tris=[[(x-s,y+h),(x-s,y-h),(x,y)],[(x+s,y+h),(x+s,y-h),(x,y)]]
    else: tris=[[(x-h,y+s),(x+h,y+s),(x,y)],[(x-h,y-s),(x+h,y-s),(x,y)]]
    for t in tris: ax.add_patch(Polygon(t,fc="white",ec=BK,lw=0.9,zorder=4))
    if kind in("ctl","onoff"):
        if o=="h": sx,sy=0,act*(h+0.1); ex,ey=0,act*(h+2.6)
        else: sx,sy=act*(h+0.1),0; ex,ey=act*(h+2.6),0
        ax.plot([x+sx,x+ex],[y+sy,y+ey],color=BK,lw=0.9,zorder=4)
        if kind=="ctl":
            ang=90 if o=="h" else 0
            if o=="h":
                th1,th2=(0,180) if act==1 else (180,360)
                ax.add_patch(Wedge((x,y+ey),1.9,th1,th2,fc="white",ec=BK,lw=0.9,zorder=4))
            else:
                th1,th2=(270,450) if act==1 else (90,270)
                ax.add_patch(Wedge((x+ex,y),1.9,th1,th2,fc="white",ec=BK,lw=0.9,zorder=4))
        else:
            if o=="h": ax.add_patch(Rectangle((x-1.3,y+ey-(0 if act==1 else 2.6)),2.6,2.6,fc="white",ec=BK,lw=0.9,zorder=4))
            else: ax.add_patch(Rectangle((x+ex-(0 if act==1 else 2.6),y-1.3),2.6,2.6,fc="white",ec=BK,lw=0.9,zorder=4))
    if tag:
        if tagpos: T(ax,tagpos[0],tagpos[1],tag,fs=fs)
        else: T(ax,x,y-3.6,tag,fs=fs) if o=="h" else T(ax,x-(4.2 if act==1 else -4.2),y,tag,fs=fs,ha="right" if act==1 else "left")
def pump(ax,x,y,tag,d="r",r=3.0):
    ax.add_patch(Circle((x,y),r,fc="white",ec=BK,lw=1.1,zorder=4))
    t={"r":[(x-1.5,y+1.9),(x-1.5,y-1.9),(x+2.1,y)],"l":[(x+1.5,y+1.9),(x+1.5,y-1.9),(x-2.1,y)],"d":[(x-1.9,y+1.5),(x+1.9,y+1.5),(x,y-2.1)]}[d]
    ax.add_patch(Polygon(t,fc="white",ec=BK,lw=0.9,zorder=5))
    T(ax,x,y-r-1.8,tag,fs=5.8,b=True)
def tank(ax,x,y,w,h,tag,name,agit=False,jacket=False,inside=True,tf=6.4):
    eh=2.4
    for yy in (y-h/2,y+h/2): ax.add_patch(Ellipse((x,yy),w,eh*2/1.0,fc="white",ec=BK,lw=1.2,zorder=3))
    ax.add_patch(Rectangle((x-w/2,y-h/2),w,h,fc="white",ec="none",zorder=3.5))
    ax.plot([x-w/2,x-w/2],[y-h/2,y+h/2],color=BK,lw=1.2,zorder=3.6); ax.plot([x+w/2,x+w/2],[y-h/2,y+h/2],color=BK,lw=1.2,zorder=3.6)
    if jacket:
        ax.add_patch(Rectangle((x-w/2-1.3,y-h/2+1),w+2.6,h*0.62,fc="none",ec=BK,lw=0.7,zorder=3.7,ls=(0,(3,1.5))))
    if agit:
        ax.plot([x,x],[y+h/2+eh,y-h/2+3.2],color=BK,lw=1.0,zorder=4)
        ax.plot([x-2.4,x+2.4],[y-h/2+3.2]*2,color=BK,lw=1.6,zorder=4)
        ax.add_patch(Circle((x,y+h/2+eh+1.7),1.7,fc="white",ec=BK,lw=0.9,zorder=4)); T(ax,x,y+h/2+eh+1.7,"M",fs=5)
    if inside:
        T(ax,x,y+0.6,tag,fs=tf+0.4,b=True); T(ax,x,y-1.8,name,fs=tf-0.8)
def hx(ax,x1,y1,x2,y2,tag,name):
    ax.add_patch(Rectangle((x1,y1),x2-x1,y2-y1,fc="white",ec=BK,lw=1.2,zorder=3))
    n=6
    for i in range(1,n):
        xx=x1+(x2-x1)*i/n; ax.plot([xx,xx],[y1+1.2,y2-1.2],color=BK,lw=0.6,zorder=3.5)
    T(ax,(x1+x2)/2,y2+3.4,tag,fs=6.2,b=True); T(ax,(x1+x2)/2,y2+1.2,name,fs=5.4)
def trap(ax,x,y):
    ax.add_patch(Circle((x,y),1.5,fc="white",ec=BK,lw=0.9,zorder=4)); T(ax,x,y,"T",fs=4.5)
def offpage(ax,x,y,txt,d="r"):
    w=11;h=6
    pts=[(x,y+h/2),(x+w-3,y+h/2),(x+w,y),(x+w-3,y-h/2),(x,y-h/2)] if d=="r" else [(x+w,y+h/2),(x+3,y+h/2),(x,y),(x+3,y-h/2),(x+w,y-h/2)]
    ax.add_patch(Polygon(pts,fc="white",ec=BK,lw=1.0,zorder=4)); T(ax,x+w/2+(0 if d=="r" else 1),y,txt,fs=5.3,b=True)
def frame(ax,sheet,title,sub):
    ax.add_patch(Rectangle((1.5,1.5),197,127,fc="none",ec=BK,lw=1.8,zorder=1))
    # cuadro de rotulacion
    x0,y0,w,h=128,1.5,70.5,19
    ax.add_patch(Rectangle((x0,y0),w,h,fc="white",ec=BK,lw=1.2,zorder=2))
    for yy in (y0+6.3,y0+12.6): ax.plot([x0,x0+w],[yy,yy],color=BK,lw=0.7,zorder=2)
    ax.plot([x0+38,x0+38],[y0,y0+12.6],color=BK,lw=0.7,zorder=2); ax.plot([x0+54,x0+54],[y0,y0+6.3],color=BK,lw=0.7,zorder=2)
    T(ax,x0+w/2,y0+15.8,title,fs=8.4,b=True)
    T(ax,x0+w/2,y0+9.5,sub,fs=6.2)
    T(ax,x0+19,y0+3.2,"Línea 3: Kumis",fs=5.6); T(ax,x0+46,y0+3.2,"Rev. A",fs=5.6); T(ax,x0+62,y0+3.2,"Hoja "+sheet,fs=6,b=True)
def legend(ax):
    x0,y0=4,2.5; w,h=120,17
    ax.add_patch(Rectangle((x0,y0),w,h,fc="white",ec=BK,lw=0.9,zorder=2)); T(ax,x0+3,y0+h-2,"Convenciones",fs=6.4,b=True,ha="left")
    # lineas
    items=[("p","Producto",y0+h-5.6),("ah","Agua helada / caliente",y0+h-8.6),("v","Agua caliente / vapor",y0+h-11.6),("cip","CIP",y0+h-14.4)]
    for k,l,yy in items:
        P(ax,[(x0+3,yy),(x0+12,yy)],k,3); T(ax,x0+14,yy,l,fs=5.4,ha="left")
    P(ax,[(x0+45,y0+h-5.6),(x0+54,y0+h-5.6)],"sig",3); T(ax,x0+56,y0+h-5.6,"Señal eléctrica",fs=5.4,ha="left")
    P(ax,[(x0+45,y0+h-8.6),(x0+54,y0+h-8.6)],"imp",3); T(ax,x0+56,y0+h-8.6,"Conexión a proceso",fs=5.4,ha="left")
    bub(ax,x0+48,y0+h-12.2,"","",False,r=1.9); T(ax,x0+56,y0+h-12.2,"Instrumento de campo",fs=5.4,ha="left")
    bub(ax,x0+48,y0+h-15.6,"","",True,r=1.9); T(ax,x0+56,y0+h-15.6,"Instrumento en SCADA/PLC",fs=5.4,ha="left")
    valve(ax,x0+90,y0+h-5.6); T(ax,x0+94,y0+h-5.6,"Válvula manual",fs=5.4,ha="left")
    valve(ax,x0+90,y0+h-10.6,kind="ctl"); T(ax,x0+94,y0+h-10.6,"Válvula de control",fs=5.4,ha="left")
    valve(ax,x0+90,y0+h-15.0,kind="onoff"); T(ax,x0+94,y0+h-15.0,"Válvula on/off",fs=5.4,ha="left")
