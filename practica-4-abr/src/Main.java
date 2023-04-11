/**
 * 1.a.
 * Vamos a modelar a nuestra queridísima golondrina, Pepita.
 * *
 * Sabemos que Pepita, como toda ave, sabe volar una cierta cantidad de
 * kilómetros y comer una cantidad de gramos de comida.
 * *
 * Cada vez que come, pepita repone energía (a razón de una unidad por
 * gramo ingerido) y cada vez que vuela, gasta energía (a razón de 3
 * unidades por cada kilómetro recorrido).
 * *
 * Además, cuando un ave nace, es bien sabido que inicia su ciclo de
 * vida con 2 unidades de energía.
 * *
 * Lo que queremos es un programa donde hagamos comer a pepita 5 gramos
 * de comida, luego la hagamos volar 1 kilómetro, y después la hagamos
 * comer 20 gramos y volar otros 2 kilómetros.
 * *
 * Pepita debe saber decirnos cuánta energía tiene al final del día.
 * *
 * 1.b
 * Nuestro modelo es simple, pero hay restricciones obvias que tal vez
 * no hayamos tenido en cuenta.
 * Sí un ave quiere volar pero no tiene energía, entonces no debería
 * hacer nada.
 * *
 * 1.c
 * Como otras golondrinas, Pepita gusta de pescar. Cuando atrapa un pez,
 * se lo come, y aumenta su energía en 10.
 * *
 * Sin embargo, solo atrapa un pez una de cada 10 veces que intenta pescar,
 * por lo que no siempre es una tarea fructifera.
 * *
 * Cada vez que intenta pescar, consume dos unidades de energía. Pepón,
 * otra golondrina, es el mejor pescador, y solo le cuesta una unidad de
 * energía por cada vez que pesca.
 * *
 * 1.d
 * Bombón es una paloma. las palomas, también son aves, y por tanto vuelan y
 * comen.
 * Pero además les gusta defecar en cualquier estatua, busto o monumento que
 * encuentren en la ciudad. Cada vez que va al baño, la paloma decrementa su
 * energía en 1.
 * *
 * 1.e
 * Queremos agregar a la aplicación un logger, que vaya dándonos información
 * acerca de cada evento que ocurre en la misma. El logger es el mismo para
 * todo el sistema, y simplemente debería saber responder a “showInfo”,
 * “showWarn” y “showError”, en donde muestra en pantalla un mensaje que
 * comienza con “INFO: “, “WARN: “ o “ERROR: “ según corresponda.
 * *
 * 1.f
 * El logger debería poder ser configurado al arranque en uno de tres modos,
 * INFO, WARN o ERROR. Sí está configurado como INFO, todo mensaje debe ser
 * mostrado, sí está configurado como WARN, solo los mensajes de showWarn y
 * showError deberían mostrarse, y sí está configurado como ERROR, solo los
 * mensajes de showError deberían mostrarse.
 * */

public class Main {

    public static void main(String[] args) {
        Logger.config(Logger.Level.INFO, System.out);
        Logger.showInfo("Una informacion 1.");
        Logger.showWarn("Un warning 1.");
        Logger.showError("Un error 1.");
        Golondrina pepita = new Golondrina(1);
        Golondrina pepon = new Golondrina(2);
        Paloma bombon = new Paloma();
        bombon.defecar();
        pepita.comer(5);
        Logger.showInfo("Una informacion 2.");
        Logger.showWarn("Un warning 2.");
        Logger.showError("Un error 2.");
        pepita.volar(1);
        pepita.comer(20);
        pepita.volar(2);
        pepon.pescar();
        Logger.showInfo("La energia de pepita es " + pepita.getEnergia());
        Logger.showWarn("La energia de bombon es " + bombon.getEnergia());
        Logger.showError("La energia de pepon es " + pepon.getEnergia());

    }
}