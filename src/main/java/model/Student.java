package model;

import org.hibernate.annotations.Cache;
import org.hibernate.annotations.CacheConcurrencyStrategy;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Table;

import com.google.common.base.Objects;


@Entity
@Table(name = "student")
@Cache(usage = CacheConcurrencyStrategy.NONSTRICT_READ_WRITE)
public class Student extends BaseEntity {

    @Column(name = "name", nullable = false, unique=true, length=50)
    private String name;

    @Column(name = "field", nullable = false, length=80)
    private String field;

    public Student(){}

    public Student(String name, String field){
        this.name = name;
        this.field = field;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }


    @Override
    public String toString() {
        return Objects.toStringHelper(this)
                .add("Name", name)
                .add("Field", field)
                .toString();
    }
}
