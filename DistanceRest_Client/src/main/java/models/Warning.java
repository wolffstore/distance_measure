package models;

public class Warning {

    private double distance;
    private String message;
    private int corridor;

    public Warning(double distance,int corridor) {
        this.distance = distance;
        this.message = getMessage();
        this.corridor = corridor;
    }

    public String getMessage() {
        return "You are "+ getDistance() + "m from corridor:-"+ getCorridor()+"-";
    }

    public void setDistance(double distance) {
        this.distance = distance;
    }

    public void setCorridor(int corridor) {
        this.corridor = corridor;
    }

    public double getDistance() {
        return distance;
    }

    public int getCorridor() {
        return corridor;
    }

    @Override
    public String toString() {
        return "models.Warning{" +
                "distance=" + distance +
                ", message='" + message + '\'' +
                ", corridor=" + corridor +
                '}';
    }
}
