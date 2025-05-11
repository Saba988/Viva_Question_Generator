import streamlit as st
import random

# Apply custom page config
st.set_page_config(
    page_title="Viva Question Generator",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sample questions categorized by difficulty level and section
VIVA_QUESTIONS = {
    "Traditional OOP Part 1": {
        "easy": [
            ("What is a class?", "A class is a blueprint for creating objects."),
            ("What are attributes in OOP?", "Attributes are variables that hold data associated with a class or object."),
            ("What are methods in OOP?", "Methods are functions defined inside a class that operate on the attributes of the class or object."),
            ("What is inheritance?", "Inheritance allows one class to inherit attributes and methods from another."),
            ("What is encapsulation?", "Encapsulation is the bundling of data with methods that operate on that data."),
        ],
        "intermediate": [
            ("What is polymorphism?", "Polymorphism allows different objects to be treated as instances of the same class through a common interface."),
            ("What is method overriding?", "Method overriding occurs when a subclass provides a specific implementation of a method defined in its superclass."),
            ("What are access modifiers?", "Access modifiers determine the visibility of attributes and methods, such as public, private, and protected."),
            ("What is constructor overloading?", "Constructor overloading allows a class to have multiple constructors with different parameters."),
            ("What is aggregation?", "Aggregation is a special type of association where an object is composed of other objects, but they can exist independently."),
        ],
        "advanced": [
            ("What is the Singleton design pattern?", "A Singleton pattern ensures that a class has only one instance."),
            ("What is the Factory design pattern?", "The Factory pattern is used to create objects in a superclass but allow subclasses to alter the type of created objects."),
            ("What is dependency injection?", "Dependency injection allows an object to receive its dependencies from an external source rather than creating them internally."),
            ("What is the Adapter design pattern?", "The Adapter pattern allows incompatible interfaces to work together by providing a wrapper."),
            ("What is the Observer pattern?", "The Observer pattern allows an object to notify a set of observers when it changes state."),
        ]
    },
    "Traditional OOP Part 2": {
        "easy": [
            ("What is an interface?", "An interface defines a contract that a class must follow but doesn't provide implementation."),
            ("What is a virtual method?", "A virtual method can be overridden in a subclass to provide a specific implementation."),
            ("What is a destructor?", "A destructor is a special method used to clean up resources when an object is destroyed."),
            ("What is a class variable?", "A class variable is a variable that is shared among all instances of the class."),
            ("What is an instance variable?", "An instance variable is a variable that is unique to each instance of a class."),
        ],
        "intermediate": [
            ("What is multiple inheritance?", "Multiple inheritance allows a class to inherit from more than one base class."),
            ("What is method resolution order (MRO)?", "MRO determines the order in which classes are searched when calling a method in an inheritance hierarchy."),
            ("What is a class factory?", "A class factory is a function that returns a class based on some conditions."),
            ("What is delegation?", "Delegation is an OOP technique where an object hands off tasks to another object."),
            ("What is a prototype design pattern?", "A prototype design pattern is used to create new objects by copying an existing object."),
        ],
        "advanced": [
            ("What is a metaclass?", "A metaclass defines the behavior of a class in Python."),
            ("What is the Flyweight design pattern?", "The Flyweight pattern is used to reduce the memory usage by sharing common object data."),
            ("What is the Bridge design pattern?", "The Bridge pattern separates abstraction from implementation, allowing them to vary independently."),
            ("What is a command design pattern?", "The Command pattern encapsulates a request as an object, allowing for parameterization of clients with queues, requests, and operations."),
            ("What is a composite design pattern?", "The Composite pattern allows you to compose objects into tree-like structures to represent part-whole hierarchies."),
        ]
    }
}

# Streamlit UI
def app():
    # Sidebar for selections
    st.sidebar.title("🧭 Navigation")
    st.sidebar.markdown("Select your options below:")

    level = st.sidebar.radio("📊 Select Difficulty Level", ["easy", "intermediate", "advanced"])
    topic = st.sidebar.selectbox("📚 Select Topic", list(VIVA_QUESTIONS.keys()))
    question_count = st.sidebar.slider("🔢 Number of Questions", 1, 5, 5)

    st.title("🧠 AI-Powered Viva Question Generator")
    st.markdown("Generate viva questions on Traditional OOP topics based on your selected difficulty level.")

    if st.button("🚀 Generate Questions"):
        questions = random.sample(VIVA_QUESTIONS[topic][level], min(question_count, len(VIVA_QUESTIONS[topic][level])))
        for i, (q, a) in enumerate(questions, 1):
            with st.expander(f"**Q{i}: {q}**"):
                st.markdown(f"**Answer:** {a}")

if __name__ == "__main__":
    app()
