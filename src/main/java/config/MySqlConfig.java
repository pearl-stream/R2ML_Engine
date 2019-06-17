package config;

import com.github.fluent.hibernate.cfg.scanner.EntityScanner;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.io.File;

public class MySqlConfig {

    private static SessionFactory sessionFactory;

    public static Configuration getConfiguration() {
        return new Configuration()
                .configure(new File("./src/main/resources/META-INF/hibernate.cfg.xml"));
    }

    public static SessionFactory getSessionFactory() {
        Configuration configuration = getConfiguration();
        EntityScanner.scanPackages("model").addTo(configuration);
        return configuration.buildSessionFactory();
    }
}
