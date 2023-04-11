import java.util.Random;

public class Golondrina extends Ave {
    private int costoPesca;
    private int habilidad;
    public Golondrina(int costoPesca) {
        this.costoPesca = costoPesca;
        this.habilidad = 1;
    }
    public boolean puedePescar() {
        return this.getEnergia() >= 2;
    }
    private boolean tuvoSuertePescando() {
        double rand = (new Random()).nextDouble();
        return rand < (1.0/this.habilidad);
    }
    public void pescar() {
        this.decEnergia(this.costoPesca);
        Logger.showInfo("En la clase Golondrina, alguna intento pescar un pez");
        if (this.tuvoSuertePescando()) {
            this.comerPez();
        }
    }
    private void comerPez() {
        this.comer(10);
    }
}
