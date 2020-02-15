package controllers;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import models.Warning;
import services.DistanceRetriever;
import services.MediaManipulator;
import services.SoundBeeper;

import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;
import java.util.Timer;
import java.util.TimerTask;

public class WarningController implements Initializable {

    private boolean isOn;
    private MediaManipulator mediaManipulator;
    private DistanceRetriever distanceRetriever;
    private int sensorMode;

    @FXML
    private ComboBox<Integer> combobox;
    @FXML
    private AnchorPane anchorpane;

    @FXML
    private Label warning;

    @FXML
    private Button power;

    @FXML
    void power(ActionEvent event) {
        //Toggle the thread
       this.isOn = !this.isOn;
       if (this.isOn){
            warn();
       }
    }

    public void warn(){
        //if it is on constantly check the distance and give the warnign
        final Timer timer = new Timer();

        TimerTask tasknew = new TimerTask() {
            @Override
            public void run() {
                if (isOn) {
                    if(combobox.getSelectionModel().getSelectedItem() == 1){
                        Warning warningObj = distanceRetriever.getDistance();
                        mediaManipulator.setBackgroundColor(anchorpane,warning,warningObj);
                    }else {
                        List<Warning> warningList = distanceRetriever.getDistances();
                        mediaManipulator.setBackgroundColorMany(anchorpane,warning,warningList);
                    }

                } else {
                    warning.setText("Welcome to Wolfstores collision detector V.- 0.1 \n     -Please be careful how you drive-");
                    anchorpane.setStyle("-fx-background-color: #00ff80");
                    timer.cancel();//cancel the timer
                    timer.purge();
                }

            }
        };
        // scheduling the task at interval
        timer.schedule(tasknew, 0, 10);
    }


    public void initialize(URL location, ResourceBundle resources) {
        this.sensorMode = 0;
        this.combobox.getItems().addAll(1,2);
        this.isOn = false;
        this.mediaManipulator = new MediaManipulator(new SoundBeeper());
        this.distanceRetriever = new DistanceRetriever();
        this.warning.setText("Welcome to Wolfstores collision detector V.- 0.1 \n -Please be careful how you drive-");
        this.anchorpane.setStyle("-fx-background-color: #00ff80");
        this.power.setStyle(
                "-fx-background-radius: 30em; " +
                        "-fx-min-width: 60px; " +
                        "-fx-min-height: 60px; " +
                        "-fx-max-width: 60px; " +
                        "-fx-max-height: 60px;"
        );
    }
}
