package services;


import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;

import java.io.FileInputStream;
import java.io.FileNotFoundException;



public class SoundBeeper {
    private boolean isPlaying;
    private Player player;

    public SoundBeeper() {
        this.isPlaying = false;
    }

    public void setPlaying(boolean playing) {
        isPlaying = playing;
        this.player = createPlayer();
    }

    public boolean isPlaying() {
        return isPlaying;
    }

    public Player getPlayer() {
        return player;
    }

    public Player createPlayer() {
        FileInputStream in = null;
        Player player = null;

        try {
            in = new FileInputStream("Beep.mp3");
            player = new Player(in);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (JavaLayerException e) {
            e.printStackTrace();
        }

        return player;
    }

    /**
     * Play a beep sound
     */
    public void playSound() {
        setPlaying(true);
        if (isPlaying) {
            try {
               this.player.play();
            } catch (JavaLayerException e) {
                e.printStackTrace();
            }
        }

    }
}
