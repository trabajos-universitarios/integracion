
package BuenosAires.ServiceClient.ServicioProducto;

import java.net.MalformedURLException;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import javax.xml.ws.WebEndpoint;
import javax.xml.ws.WebServiceClient;
import javax.xml.ws.WebServiceException;
import javax.xml.ws.WebServiceFeature;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.3.5
 * Generated source version: 2.2
 * 
 */
@WebServiceClient(name = "ServicioProducto", targetNamespace = "http://tempuri.org/", wsdlLocation = "http://localhost:4795/ServicioProducto.svc?wsdl")
public class ServicioProducto
    extends Service
{

    private final static URL SERVICIOPRODUCTO_WSDL_LOCATION;
    private final static WebServiceException SERVICIOPRODUCTO_EXCEPTION;
    private final static QName SERVICIOPRODUCTO_QNAME = new QName("http://tempuri.org/", "ServicioProducto");

    static {
        URL url = null;
        WebServiceException e = null;
        try {
            url = new URL("http://localhost:4795/ServicioProducto.svc?wsdl");
        } catch (MalformedURLException ex) {
            e = new WebServiceException(ex);
        }
        SERVICIOPRODUCTO_WSDL_LOCATION = url;
        SERVICIOPRODUCTO_EXCEPTION = e;
    }

    public ServicioProducto() {
        super(__getWsdlLocation(), SERVICIOPRODUCTO_QNAME);
    }

    public ServicioProducto(WebServiceFeature... features) {
        super(__getWsdlLocation(), SERVICIOPRODUCTO_QNAME, features);
    }

    public ServicioProducto(URL wsdlLocation) {
        super(wsdlLocation, SERVICIOPRODUCTO_QNAME);
    }

    public ServicioProducto(URL wsdlLocation, WebServiceFeature... features) {
        super(wsdlLocation, SERVICIOPRODUCTO_QNAME, features);
    }

    public ServicioProducto(URL wsdlLocation, QName serviceName) {
        super(wsdlLocation, serviceName);
    }

    public ServicioProducto(URL wsdlLocation, QName serviceName, WebServiceFeature... features) {
        super(wsdlLocation, serviceName, features);
    }

    /**
     * 
     * @return
     *     returns IServicioProducto
     */
    @WebEndpoint(name = "BasicHttpBinding_IServicioProducto")
    public IServicioProducto getBasicHttpBindingIServicioProducto() {
        return super.getPort(new QName("http://tempuri.org/", "BasicHttpBinding_IServicioProducto"), IServicioProducto.class);
    }

    /**
     * 
     * @param features
     *     A list of {@link javax.xml.ws.WebServiceFeature} to configure on the proxy.  Supported features not in the <code>features</code> parameter will have their default values.
     * @return
     *     returns IServicioProducto
     */
    @WebEndpoint(name = "BasicHttpBinding_IServicioProducto")
    public IServicioProducto getBasicHttpBindingIServicioProducto(WebServiceFeature... features) {
        return super.getPort(new QName("http://tempuri.org/", "BasicHttpBinding_IServicioProducto"), IServicioProducto.class, features);
    }

    private static URL __getWsdlLocation() {
        if (SERVICIOPRODUCTO_EXCEPTION!= null) {
            throw SERVICIOPRODUCTO_EXCEPTION;
        }
        return SERVICIOPRODUCTO_WSDL_LOCATION;
    }

}
