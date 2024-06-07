import java.util.ArrayList;
import java.util.List;

class Course {
    private String courseCode;
    private String title;
    private String description;
    private int capacity;
    private List<String> schedule;
    private List<String> registeredStudents;

    public Course(String courseCode, String title, String description, int capacity, List<String> schedule) {
        this.courseCode = courseCode;
        this.title = title;
        this.description = description;
        this.capacity = capacity;
        this.schedule = schedule;
        this.registeredStudents = new ArrayList<>();
    }

    public String getCourseCode() {
        return courseCode;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public int getCapacity() {
        return capacity;
    }

    public List<String> getSchedule() {
        return schedule;
    }

    public List<String> getRegisteredStudents() {
        return registeredStudents;
    }

    public boolean registerStudent(String studentId) {
        if (registeredStudents.size() < capacity) {
            registeredStudents.add(studentId);
            return true;
        } else {
            return false; // Course is full
        }
    }

    public boolean removeStudent(String studentId) {
        return registeredStudents.remove(studentId);
    }
}

class Student {
    private String studentId;
    private String name;
    private List<String> registeredCourses;

    public Student(String studentId, String name) {
        this.studentId = studentId;
        this.name = name;
        this.registeredCourses = new ArrayList<>();
    }

    public String getStudentId() {
        return studentId;
    }

    public String getName() {
        return name;
    }

    public List<String> getRegisteredCourses() {
        return registeredCourses;
    }

    public void registerCourse(String courseCode) {
        registeredCourses.add(courseCode);
    }

    public void dropCourse(String courseCode) {
        registeredCourses.remove(courseCode);
    }
}

public class CourseRegistrationSystem {
    public static void main(String[] args) {
        // Create courses
        List<String> schedule = new ArrayList<>();
        schedule.add("Monday, 10:00 AM");
        schedule.add("Wednesday, 2:00 PM");
        Course javaCourse = new Course("CS101", "Java Programming", "Introduction to Java programming", 20, schedule);

        // Create students
        Student student1 = new Student("1001", "Alice");
        Student student2 = new Student("1002", "Bob");

        // Register students for courses
        javaCourse.registerStudent(student1.getStudentId());
        javaCourse.registerStudent(student2.getStudentId());
        student1.registerCourse(javaCourse.getCourseCode());
        student2.registerCourse(javaCourse.getCourseCode());

        // Print course details
        System.out.println("Course Code: " + javaCourse.getCourseCode());
        System.out.println("Title: " + javaCourse.getTitle());
        System.out.println("Description: " + javaCourse.getDescription());
        System.out.println("Capacity: " + javaCourse.getCapacity());
        System.out.println("Schedule: " + javaCourse.getSchedule());
        System.out.println("Registered Students: " + javaCourse.getRegisteredStudents());

        // Print student details
        System.out.println("Student ID: " + student1.getStudentId());
        System.out.println("Name: " + student1.getName());
        System.out.println("Registered Courses: " + student1.getRegisteredCourses());

        // Drop a course for a student
        student1.dropCourse(javaCourse.getCourseCode());
        javaCourse.removeStudent(student1.getStudentId());
        System.out.println("After dropping a course:");
        System.out.println("Registered Courses for " + student1.getName() + ": " + student1.getRegisteredCourses());
        System.out.println("Registered Students for " + javaCourse.getTitle() + ": " + javaCourse.getRegisteredStudents());
    }
}
