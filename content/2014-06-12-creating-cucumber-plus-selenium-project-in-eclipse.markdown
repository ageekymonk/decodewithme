---
layout: post
title: "creating cucumber+selenium Project in eclipse"
date: 2014-06-15 02:41:05 +1000
comments: true
categories:
published: true
---

To use eclipse with java cucumber + selenium we need to install the following eclipse plugins. The following configuration
has been tested with eclipse (kepler)

1. Eclipse maven plugin
        The plugin site is:

            http://download.eclipse.org/technology/m2e/releases
2. Eclipse cucumber plugin
        The plugin site is

            http://cucumber.github.com/cucumber-eclipse/update-site

3. Next step is to create a maven project with cucumber and selenium as dependencies. To create a maven project.
   a. Go to File -> New -> Other.
        {% img center /images/cucumber_selenium_maven_step1.png %}
   b. Select Maven Project and click Next.

        {% img center /images/cucumber_selenium_maven_step2.png %}

   c. Select the checkbox "Create a Simple Project" and click Next

        {% img center /images/cucumber_selenium_maven_step3.png %}

   d. Select a unique name for GroupId. It is generally written of the form **org.yourOrganisationName.ModuleName**
      Select a ArtifactId. This is the name with which the final output jar file will be created.
      By default ArtifactId is taken as default package.
      Select a Name, which can be anything to describe it. Then click Finish.

        {% img center /images/cucumber_selenium_maven_step4.png %}


4. Open the pom.xml by double clicking it. And seleting the pom.xml tab at the bottom of the opened file.
5. And Now add cucumber as maven dependency. Copy and paste the following lines in pom.xml between <project> </project>

        <dependencies>
            <dependency>
                <groupId>info.cukes</groupId>
                <artifactId>cucumber-picocontainer</artifactId>
                <version>1.1.5</version>
                <scope>test</scope>
            </dependency>
            <dependency>
                <groupId>info.cukes</groupId>
                <artifactId>cucumber-junit</artifactId>
                <version>1.1.5</version>
                <scope>test</scope>
            </dependency>
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>4.11</version>
                <scope>test</scope>
            </dependency>
        </dependencies>



    For the latest version check the site.

            http://cukes.info/install-cucumber-jvm.html

5. Now Add selenium as maven dependency. Copy and paste the following lines in pom.xml between <dependencies> </dependencies>

            <dependency>
                <groupId>org.seleniumhq.selenium</groupId>
                <artifactId>selenium-java</artifactId>
                <version>2.42.2</version>
            </dependency>

    For the latest version check the site.

            http://docs.seleniumhq.org/download/maven.jsp

    Your final pom file should look like this.

            <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
              <modelVersion>4.0.0</modelVersion>
              <groupId>org.ageekymonk.Myapp</groupId>
              <artifactId>mykillerapp</artifactId>
              <version>0.0.1-SNAPSHOT</version>
              <name>My Killer Web App</name>
              <dependencies>
                <dependency>
                    <groupId>info.cukes</groupId>
                    <artifactId>cucumber-picocontainer</artifactId>
                    <version>1.1.5</version>
                    <scope>test</scope>
                </dependency>
                <dependency>
                    <groupId>info.cukes</groupId>
                    <artifactId>cucumber-junit</artifactId>
                    <version>1.1.5</version>
                    <scope>test</scope>
                </dependency>
                <dependency>
                    <groupId>junit</groupId>
                    <artifactId>junit</artifactId>
                    <version>4.11</version>
                    <scope>test</scope>
                </dependency>
                <dependency>
                    <groupId>org.seleniumhq.selenium</groupId>
                    <artifactId>selenium-java</artifactId>
                    <version>2.42.2</version>
                </dependency>
            </dependencies>
            </project>

6. Now right click pom.xml and select Run As -> Maven Install
   {% img center /images/cucumber_selenium_maven_step5.png %}

7. Next step is to create a Test Runner class, which runs all the cucumber features.
    Right click on src/test/java. Select New -> class. You can provide any name for the class. I have provided **RunTests**.
    Open the file and add the following lines to it.

        package mykillerapp;

        import cucumber.api.CucumberOptions;
        import cucumber.api.junit.Cucumber;
        import org.junit.runner.RunWith;

        @RunWith(Cucumber.class)
        @CucumberOptions(monochrome = true)
        public class RunTests {
        }

7. Next step is to create a Feature file for our tests. Lets say we want to open a google page and search for cucumber.
    Right click on src/test/resources. Select New -> File. Lets say we create a file called **google.Feature**.
    Add the following content to it.

        Feature: Searching in Google

        Scenario: Searching for any text
        	Given i open the site "google.com"
        	When I input for the string "selenium" in google search box
        	Then I should get results for the string

8. Now we can run the feature. Right click on the file **google.Feature** and select Run As -> Run Configurations.
    {% img center /images/cucumber_selenium_maven_step6.png %}

    Select Cucumber Feature. Then select New Launch Configuration.
    {% img center /images/cucumber_selenium_maven_step7.png %}

    Give a name **search Feature** and click Apply and then click Run.
    {% img center /images/cucumber_selenium_maven_step8.png %}

    You will get something like this about missing steps on the console below.

        Feature: Searching in Google

          Scenario: Searching for any text                              # /Users/ramz/Projects/oss/workspace/mykillerapp/src/test/resources/google.Feature:3
            Given i open the site "google.com"
            When I input for the string "selenium" in google search box
            Then I should get results for the string

        1 Scenarios (1 undefined)
        3 Steps (3 undefined)
        0m0.000s


        You can implement missing steps with the snippets below:

        @Given("^i open the site \"([^\"]*)\"$")
        public void i_open_the_site(String arg1) throws Throwable {
            // Express the Regexp above with the code you wish you had
            throw new PendingException();
        }

        @When("^I input for the string \"([^\"]*)\" in google search box$")
        public void I_input_for_the_string_in_google_search_box(String arg1) throws Throwable {
            // Express the Regexp above with the code you wish you had
            throw new PendingException();
        }

        @Then("^I should get page title as \"([^\"]*)\"$")
        public void I_should_get_page_title_as(String arg1) throws Throwable {
            // Express the Regexp above with the code you wish you had
            throw new PendingException();
        }



9. Now we need to implement the steps.Right click on src/test/java. Select New -> class. You can provide any name for the class.
I have provided **SearchStepDefs**. Here we are going to implement the steps. You can copy the snippet provided when you run the feature.
Just replace the PendingException() with your implementation for the step


        package mykillerapp;

        import cucumber.api.java.en.Given;
        import cucumber.api.java.en.When;
        import cucumber.api.java.en.Then;

        import org.junit.Assert;
        import org.openqa.selenium.By;
        import org.openqa.selenium.WebDriver;
        import org.openqa.selenium.WebElement;
        import org.openqa.selenium.firefox.FirefoxDriver;

        public class SearchStepDefs {
        	WebDriver driver;
        	@Given("^i open the site \"([^\"]*)\"$")
        	public void i_open_the_site(String arg1) throws Throwable {
        	    driver = new FirefoxDriver();
        	    driver.get(arg1);
        	}

        	@When("^I input for the string \"([^\"]*)\" in google search box$")
        	public void I_input_for_the_string_in_google_search_box(String arg1) throws Throwable {
        		WebElement element = driver.findElement(By.id("gbqfq"));
        		element.sendKeys(arg1);
        		element.submit();
        	}


        	@Then("^I should get page title as \"([^\"]*)\"$")
        	public void I_should_get_page_title_as(String arg1) throws Throwable {
        		Assert.assertEquals(arg1, driver.getTitle());
        		driver.quit();
        	}

        }

10. You can run the feature using Run -> Run History -> "search Feature" (This is the name you gave in run configuration)
    You should see the test pass.