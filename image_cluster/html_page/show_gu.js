//document.getElementById('img_tile').style.display="none";
var img_tile_id = ['gn_gn', 'se_gd', 'gb_gb', 'sw_gs', 'ss_ga', 'es_gj',
'sw_gr', 'ss_gc', 'gb_nw', 'gb_db', 'es_ddm', 'ss_dj',
'ws_mp', 'ws_sdm', 'gn_sc', 'es_sd', 'gb_sb', 'se_sp', 'sw_yc',
'sw_ydp', 'cs_ys', 'ws_ep', 'cs_jr', 'cs_jg', 'es_gl'];

var desc = {
  'gn_gn' : '강남구 <strong>색감</strong>',
  'se_gd': '강동구 색감'
};

for(var i=0;i<img_tile_id.length;i++){
  gu = img_tile_id[i];
  btn = document.querySelector('#btn_' + gu);
  btn.addEventListener('click', function(event) {
    img_show_hide(event);
 })
}

function img_show_hide(event) {
  var gu = event.target.parentNode.id.substr(4)
   for(var i=0;i<img_tile_id.length;i++){
     a_name_gu = document.querySelector("p#img_tile a[name="+img_tile_id[i]+"]");
     if(img_tile_id[i] === gu){
       a_name_gu.style.display="block";
//       document.querySelector('#desc').innerHTML = '카페 색감 설명 : <br>' + desc[gu];
     } else{
       a_name_gu.style.display="none";
     }
   }
}
