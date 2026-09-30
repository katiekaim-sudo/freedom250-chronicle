// Self-contained heliocentric ephemeris — Standish/JPL Keplerian elements (valid 1800–2050).
// Returns heliocentric ecliptic-of-J2000 rectangular coords (AU) + distance, and derived geo longitude.
var HELIO=(function(){
  var D2R=Math.PI/180, R2D=180/Math.PI;
  function norm(d){return ((d%360)+360)%360;}
  // a,e,I,L,peri(ϖ),node(Ω) at J2000 + rates per Julian century
  var EL={
    Mercury:[0.38709927,0.20563593,7.00497902,252.25032350,77.45779628,48.33076593, 0.00000037,0.00001906,-0.00594749,149472.67411175,0.16047689,-0.12534081],
    Venus:  [0.72333566,0.00677672,3.39467605,181.97909950,131.60246718,76.67984255, 0.00000390,-0.00004107,-0.00078890,58517.81538729,0.00268329,-0.27769418],
    Earth:  [1.00000261,0.01671123,-0.00001531,100.46457166,102.93768193,0.0, 0.00000562,-0.00004392,-0.01294668,35999.37244981,0.32327364,0.0],
    Mars:   [1.52371034,0.09339410,1.84969142,-4.55343205,-23.94362959,49.55953891, 0.00001847,0.00007882,-0.00813131,19140.30268499,0.44441088,-0.29257343],
    Jupiter:[5.20288700,0.04838624,1.30439695,34.39644051,14.72847983,100.47390909, -0.00011607,-0.00013253,-0.00183714,3034.74612775,0.21252668,0.20469106],
    Saturn: [9.53667594,0.05386179,2.48599187,49.95424423,92.59887831,113.66242448, -0.00125060,-0.00050991,0.00193609,1222.49362201,-0.41897216,-0.28867794],
    Uranus: [19.18916464,0.04725744,0.77263783,313.23810451,170.95427630,74.01692503, -0.00196176,-0.00004397,-0.00242939,428.48202785,0.40805281,0.04240589],
    Neptune:[30.06992276,0.00859048,1.77004347,-55.12002969,44.96476227,131.78422574, 0.00026291,0.00005105,0.00035372,218.45945325,-0.32241464,-0.00508664],
    Pluto:  [39.48211675,0.24882730,17.14001206,238.92903833,224.06891629,110.30393684, -0.00031596,0.00005170,0.00004818,145.20780515,-0.04062942,-0.01183482]
  };
  function kepler(M,e){ // M deg, e (unitless); returns E deg
    var Mr=norm(M); if(Mr>180)Mr-=360; Mr*=D2R;
    var E=Mr+e*Math.sin(Mr);
    for(var k=0;k<8;k++){ var dM=Mr-(E-e*Math.sin(E)); E+=dM/(1-e*Math.cos(E)); }
    return E*R2D;
  }
  function helioRect(name,jd){ // heliocentric ecliptic-J2000 rectangular {x,y,z,r}
    var T=(jd-2451545.0)/36525, el=EL[name];
    var a=el[0]+el[6]*T, e=el[1]+el[7]*T, I=el[2]+el[8]*T,
        L=el[3]+el[9]*T, peri=el[4]+el[10]*T, node=el[5]+el[11]*T;
    var w=peri-node, M=L-peri;
    var E=kepler(M,e)*D2R;
    var xp=a*(Math.cos(E)-e), yp=a*Math.sqrt(1-e*e)*Math.sin(E);
    var cw=Math.cos(w*D2R),sw=Math.sin(w*D2R),cO=Math.cos(node*D2R),sO=Math.sin(node*D2R),cI=Math.cos(I*D2R),sI=Math.sin(I*D2R);
    var x=(cw*cO-sw*sO*cI)*xp+(-sw*cO-cw*sO*cI)*yp;
    var y=(cw*sO+sw*cO*cI)*xp+(-sw*sO+cw*cO*cI)*yp;
    var z=(sw*sI)*xp+(cw*sI)*yp;
    return {x:x,y:y,z:z,r:Math.sqrt(x*x+y*y+z*z)};
  }
  // general precession J2000 -> of-date, longitude (deg)
  function prec(jd){ var T=(jd-2451545.0)/36525; return 1.396971*T+0.0003086*T*T; }
  function helioLon(name,jd){ var p=helioRect(name,jd); return norm(Math.atan2(p.y,p.x)*R2D+prec(jd)); }
  function geoLon(name,jd){ // geocentric ecliptic-of-date longitude
    if(name==="Sun"){ var Ev=helioRect("Earth",jd); return norm(Math.atan2(-Ev.y,-Ev.x)*R2D+prec(jd)); }
    var P=helioRect(name,jd), Ee=helioRect("Earth",jd);
    var gx=P.x-Ee.x, gy=P.y-Ee.y;
    return norm(Math.atan2(gy,gx)*R2D+prec(jd));
  }
  function geoDist(name,jd){ var P=helioRect(name,jd), Ee=helioRect("Earth",jd); return Math.sqrt((P.x-Ee.x)**2+(P.y-Ee.y)**2+(P.z-Ee.z)**2);}
  return {helioRect:helioRect,helioLon:helioLon,geoLon:geoLon,geoDist:geoDist,norm:norm};
})();
if(typeof module!=="undefined")module.exports=HELIO;
