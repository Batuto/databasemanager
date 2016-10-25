%rebase ./mysite/views/menu.tpl title="DataBase - Products"
%#-*-coding:utf-8-*-
<div class="row">
 <div class="col-lg-12">

        %if rows:
        <div class="panel panel-default">
        <!-- Default panel contents -->
        <div class="panel-heading">{{name}}</div>
        <table class="table">
        %for row in rows:
            <tr>
            %for x in row:
                <td>
                {{x}}
                </td>
            %end

            </tr>
        %end  # End For
        </table>
        </div>
        </div>

        %else:
            <div class="text-center">
            <h3>Tabla Sin Datos</h3>
            </div>
        %end # End Else/IF
        


 </div>
</div>
<div class="container-fluid navbar">
    
    <div class="row">
        <form method="POST" id="model">
            <div class="col-lg-4">
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


            %value = rows[count][u]

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
             %end
            <button type="submit" class="btn btn-default">Guardar</button>
         </div>
         <div class="col-lg-4">
             <div class="checkbox">
                  <label><input type="checkbox" name="Insertar"> Guardar en tabla.</label>
                </div>
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

            <form method="POST">
                <button class="btn btn-default" type="submit" form="model">Modificar</button>
                <input type="text" name="Modificar" value="Modificar" form="model" class="hidden">
            </form>

          
           </div>
        </form>
    </div>  
    <div class="row">
        <div class="col-lg-6">
        <a class="btn btn-default" href="/menu" role="button">Cancelar</a>
        </div>
        <div class="col-lg-4">
           
        </div>
        <div class="col-lg-2">
        </div>
    </div>  
</div>