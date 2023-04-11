
import java.util.Random;

public class Ave {
    private int energia;
    public Ave()
    {
        this.energia = 2;
    }
    public void comer(int gramos)
    {
        this.incEnergia(gramos);
    }
    public void volar(int kms)
    {
        this.decEnergia(kms*3);
    }
    public int getEnergia() {
        return this.energia;
    }
    private void setEnergia(int energia) {
        this.energia = energia;
    }
    private boolean hayEnergiaPara(int cantidad) {
        return this.energia >= cantidad;
    }
    protected void incEnergia(int cantidad) {
        this.setEnergia(this.getEnergia() + cantidad);
    }
    protected void decEnergia(int cantidad) {
        if (this.hayEnergiaPara(cantidad)){
            this.setEnergia(this.getEnergia() - cantidad);
            Logger.showInfo("En la clase Ave, se decremento la energia, obteniendo: " + this.getEnergia());
        }
    }
}
