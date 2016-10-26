%rebase ./mysite/views/menu.tpl title="DataBase - Products"

<div class="container-fluid navbar">
    
     <div class="row">
            <form method="POST" id="model" action="/nuevo/{{path}}">
                <div class="col-lg-4">
                    
                    <div class="form-group">
                    

                      
                      %for idx, campo in enumerate(data):
                        %in_type = "text"
                        %if campo == "Perishable":
                          %in_type = "checkbox"
                        %end # if campo

                        {{campo}}
                        <br><!--p>&#9;</p-->
                        <input type={{in_type}} name="{{campo}}">
                        <br><br>
                       %end
                    </div>


            <br>
            <button type="submit" class="btn btn-default">Guardar</button>
        </form>
         </div>
         <div class="col-lg-4">
            <a class="btn btn-default" href="/{{path}}" role="button">Cancelar</a>
          </div>

          <div class="col-lg-4">

          
           </div>
    </div>  
    
</div>
</div>