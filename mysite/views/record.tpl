%rebase ./mysite/views/menu.tpl title="DataBase - Products"

<div class="container-fluid navbar">
    
     <div class="row">
            <form method="POST" id="model" action="/guardar/{{path}}/{{row[0][1]}}">
                <div class="col-lg-4">
                    
                    <div class="form-group">
                    

                      %valx = row[0]
                      %for idx, campo in enumerate(data):
                      %in_type = "text"
                      %field_value = valx[idx]
                      %print type(field_value)
                      %if isinstance(field_value, bool):
                      %in_type = "checkbox"
            
                      %end  # if

                  {{campo}}
                  <br><!--p>&#9;</p-->
                  <input type={{in_type}} name="{{campo}}" value={{field_value}} {{'checked = "checked"' if field_value else ''}}>
                  <br><br>
                       %end
                    </div>







                %"""
                % u = 0
              %for algo in data:
                  %if algo != "Perishable":
                    %type = "text"
                   %else:
                    %type = "checkbox"
                %end


                %if algo == "Id":
                    %X = "hidden"
                    %algo = ""
                %else:
                    %X = ""
                %end


        
                %value = row[u]

                %#if value == True:
                    %#value = "checked"
                %#end
        
                <div class="form-group">

                {{algo}}
                <p>&#9;</p>
                <input type="{{type}}" name={{algo}} value="{{value}}" {{X}}>
                
                <br>
                </div>
                %u += 1
             %end  # end For
             %"""


            <br>
            <button type="submit" class="btn btn-default">Guardar</button>
        </form>
         </div>
         <div class="col-lg-4">
            <form method="POST" action="/borrar/{{path}}/{{row[0][1]}}">
               <button class="btn btn-default" type="submit">Borrar</button>
                <input type="text" name="Borrar" value="Borrar" class="hidden">
                <input type="text" name="comes_from" value="modificar" class="hidden">
            </form>  


          </div>

          <div class="col-lg-4">

             <form method="POST">
                <button class="btn btn-default" type="submit">Anterior</button>
                <input type="text" name="Anterior" value="Anterior" class="hidden">
            </form>

             <form method="POST">
                <button class="btn btn-default" type="submit">Siguiente</button>
                <input type="text" name="Siguiente" value="Siguiente" class="hidden">
            </form>

          
           </div>
    </div>  
    
</div>
</div>