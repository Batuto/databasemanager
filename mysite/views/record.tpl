%rebase ./mysite/views/menu.tpl title="DataBase - Products"

<div class="container-fluid navbar">
    
     <div class="row">
            <form method="POST" id="model" action="/guardar/{{path}}/{{row[0][1]}}">
                <div class="col-lg-4">
                    
                    <div class="form-group">
                    

                      %valx = row[0]
                      %for idx, campo in enumerate(data):
                      %in_type = "text"
                      %print idx,"idx",campo
                      %field_value = valx[idx]
                      %print type(field_value),field_value
                      %if isinstance(field_value, bool):
                      %in_type = "checkbox"
            
                      %end  # if

                  {{campo}}
                  <br><!--p>&#9;</p-->
                  <input type={{in_type}} name="{{campo}}" value={{field_value}} {{'checked = "checked"' if field_value else ''}}>
                  <br><br>
                       %end
                    </div>

            <br>
            <button type="submit" class="btn btn-default">Guardar</button>
        </form>
         </div>
         <div class="col-lg-4">
            <form method="POST" action="/borrar/{{path}}/{{row[0][1]}}">
               <button class="btn btn-default" type="submit">Borrar</button>
                <input type="text" name="Borrar" value="Borrar" class="hidden">
            </form>  
            <br>
            <a class="btn btn-default" href="/{{path}}" role="button">Cancelar</a>
          </div>

          <div class="col-lg-4">

             <form method="POST">
                <button class="btn btn-default" type="submit">Anterior</button>
                <input type="text" name="Anterior" value="Anterior" class="hidden">
            </form>
            <br>
             <form method="POST">
                <button class="btn btn-default" type="submit">Siguiente</button>
                <input type="text" name="Siguiente" value="Siguiente" class="hidden">
            </form>

          
           </div>
    </div>  
    
</div>
</div>