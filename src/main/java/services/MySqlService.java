package services;

import config.MySqlConfig;
import model.Student;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MySqlService {

    private final Logger log = LoggerFactory.getLogger(MySqlService.class);

    private SessionFactory sessionFactory = null;


    public MySqlService() {
    }

    public void saveStudent(Student student) {

        if (sessionFactory == null) {
            sessionFactory = MySqlConfig.getSessionFactory();
        }

        Transaction tx = null;
        try (Session session = sessionFactory.openSession()) {

            tx = session.beginTransaction();

            session.save(student);
            tx.commit();


        } catch (RuntimeException e) {
            assert tx != null;
            tx.rollback();
            throw e;

        }
    }


    public void exampleData() {

        List<Student> exampleList = new ArrayList<Student>(Arrays.<Student>asList(
                new Student("peter", "music"),
                new Student("michael", "informatik"),
                new Student("riddler", "informatik")
        ));

        for (Student s : exampleList) {
            this.saveStudent(s);
        }

        log.debug("Example data in DB");

    }

}
