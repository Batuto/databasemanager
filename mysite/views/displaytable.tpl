%rebase ./mysite/views/menu.tpl title="DataBase - Products"
%#-*-coding:utf-8-*-
<div class="row">
    <div class="col-lg-12">
    %print rows,"HEeeelp"
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
                            <td>
                            <a href="/modificar/{{path}}/{{row[1]}}">
                            <span class=""><p>Editar</p></span>
                            </a>
                            </td>
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
<div class="row">
    <div class="col-lg-3">
       <a class="btn btn-default" href="/nuevo/{{path}}" role="button">Nuevo</a>
                
    </div>
    <div class="col-lg-9">   
    </div>
</div>
