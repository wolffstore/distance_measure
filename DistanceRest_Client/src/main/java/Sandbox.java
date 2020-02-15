import javazoom.jl.decoder.JavaLayerException;
import models.Warning;
import services.DistanceRetriever;
import services.SoundBeeper;


import java.io.IOException;
import java.util.List;

public class Sandbox {

    public static void main(String[] args) throws IOException {
        DistanceRetriever d = new DistanceRetriever();

        List<Warning> warningList = d.getDistances();

        for(int i=0; i<15; i++){
            warningList.forEach(w -> System.out.println(w));
            System.out.println(" ");
        }


    }
}
