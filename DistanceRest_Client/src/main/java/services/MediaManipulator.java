package services;

import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import models.Warning;

import java.util.List;

public class MediaManipulator {

    private SoundBeeper beeper;

    public MediaManipulator(SoundBeeper beeper) {
        this.beeper = beeper;
    }

    public void setBackgroundColor(AnchorPane anchorPane, Label label, Warning warning){
        label.setText("");
        if(warning.getDistance() <=150.0){
            anchorPane.setStyle("-fx-background-color: #ff0000");
            label.setText("You are too close slow down\n "+warning.getMessage());
            label.setStyle("-fx-font-weight: bold");
            this.beeper.playSound();

        }else if(warning.getDistance() >150.0){
            anchorPane.setStyle("-fx-background-color: #00ff80");
            label.setText("You are fine but be careful anyways");
            label.setStyle("-fx-font-weight: bold");

            if(this.beeper.isPlaying()){
                this.beeper.getPlayer().close();
            }

        }
    }

    public void setBackgroundColorMany(AnchorPane anchorPane, Label label, List<Warning> warningList){

            for(Warning w : warningList){
                if(w.getDistance() <=150.0){
                    label.setText("");
                    anchorPane.setStyle("-fx-background-color: #ff0000");
                    label.setText("You are too close slow down\n "+w.getMessage());
                    label.setStyle("-fx-font-weight: bold");
                    this.beeper.playSound();
                }else {
                    if(this.beeper.isPlaying()){
                        this.beeper.getPlayer().close();
                    }
                }
            }
    }

}
