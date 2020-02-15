package services;

import models.Warning;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class DistanceRetriever {

    public List<Warning> getDistances(){
        List<Warning> warnings = null;
        try {
            //Make the call to the server
            URL url = new URL("http://192.168.0.144:8000/distances");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");

            //Check the response code
            if (con.getResponseCode() != 200) {
                throw new RuntimeException("Failed : HTTP error code : "
                        + con.getResponseCode());
            }

            //Create an empty string which will serve as the json
            String output = "";

            System.out.println("Output from Server .... \n");

            warnings = getWarningFromjsonMany(output,url);

            System.out.println(output);
            con.disconnect();
        } catch (MalformedURLException e) {

            e.printStackTrace();

        } catch (IOException e) {

            e.printStackTrace();

        }

        return warnings;
    }

    public Warning getDistance() {
        Warning warning = null;

        try {
            //Make the call to the server
            URL url = new URL("http://127.0.0.1:5000/distances");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Accept", "application/json");

            //Check the response code
            if (con.getResponseCode() != 200) {
                throw new RuntimeException("Failed : HTTP error code : "
                        + con.getResponseCode());
            }

            //Create an empty string which will serve as the json
            String output = "";

            System.out.println("Output from Server .... \n");

            warning = getWarningFromjson(output,url);

            System.out.println(output);
            con.disconnect();
        } catch (MalformedURLException e) {

            e.printStackTrace();

        } catch (IOException e) {

            e.printStackTrace();

        }

        return warning;
    }


    /**
     *  Returns a warning object from the given url
     * @param json
     * @param url
     * @return
     */
    public Warning getWarningFromjson(String json, URL url){
        Warning warning = null;

        try {
            //Use a scanner to save the Json into a string
            Scanner scanner = new Scanner(url.openStream());

            while(scanner.hasNext()){
                json += scanner.nextLine();
            }

            //Close the scanner to save resources
            scanner.close();

            JSONParser parser = new JSONParser();

            JSONObject obj = (JSONObject)parser.parse(json);

            double distance = Double.parseDouble(String.valueOf(obj.get("distance")));
            int corridor = Integer.parseInt(String.valueOf(obj.get("corridor")));

            warning = new Warning(distance,corridor);

        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

        return warning;
    }

    /**
     *  Returns a warning object from the given url
     * @param json
     * @param url
     * @return
     */
    public List<Warning> getWarningFromjsonMany(String json, URL url){
        List<Warning> warnings = null;

        try {
            //Use a scanner to save the Json into a string
            Scanner scanner = new Scanner(url.openStream());

            while(scanner.hasNext()){
                json += scanner.nextLine();
            }

            //Close the scanner to save resources
            scanner.close();

            JSONParser parser = new JSONParser();

            JSONObject obj = (JSONObject)parser.parse(json);
            JSONArray warningsJson = (JSONArray) obj.get("sensors");

            warnings = new ArrayList<>();

            for(int i=0; i<warningsJson.size(); i++){
                JSONObject sensorObject = (JSONObject) warningsJson.get(i);
                double distance = Double.parseDouble(String.valueOf(sensorObject.get("distance")));
                int corridor = Integer.parseInt(String.valueOf(sensorObject.get("corridor")));

                warnings.add(new Warning(distance,corridor));
            }


        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

        return warnings;
    }
}
